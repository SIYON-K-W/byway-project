from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from decimal import Decimal
from django.core.exceptions import ValidationError
from decimal import Decimal, ROUND_HALF_UP


PERCENTAGE_VALIDATOR = [MinValueValidator(0), MaxValueValidator(100)]

def validate_half_or_full_percentage(value):
    if Decimal(value) % 1 not in (Decimal('0.0'), Decimal('0.5')):
        raise ValidationError(f"Only full or half percentages are allowed. You provided {value}.")


class Language(models.Model):
    name=models.CharField(max_length=255)

    class Meta:
        db_table="web_Language"
        ordering=["name"]
        verbose_name="course_Language"
        verbose_name_plural="course_Languages"

    def __str__(self):
        return self.name

class Category(models.Model):
    name=models.CharField(max_length=255)
    logo=models.FileField(upload_to="category/icons/")
    
    class Meta:
        db_table="web_Category"
        ordering=["name"]
        verbose_name="course_category"
        verbose_name_plural="course_categories"

    def __str__(self):
        return self.name    
    
class Author(models.Model):
    name=models.CharField(max_length=255)
    profile_image=models.FileField(upload_to="course/authors/")

    class Meta:
        db_table="web_Author"
        ordering=["name"]
        verbose_name="Author"
        verbose_name_plural="Authors"

    def __str__(self):
        return self.name    


class Course(models.Model):
    title = models.CharField(max_length=255)
    card_title = models.CharField(max_length=28)
    image = models.ImageField(upload_to="course/images/")
    thumbnail_image = models.ImageField(upload_to="course/thumbnailimages/")
    description = models.TextField()
    rating = models.FloatField(validators=[MinValueValidator(1.0), MaxValueValidator(5.0)])
    rated_customers_count = models.PositiveIntegerField(default=0)
    total_hours = models.DurationField()
    author = models.ForeignKey("web.Author", on_delete=models.CASCADE, blank=True, null=True)
    category = models.ForeignKey("web.Category", on_delete=models.DO_NOTHING, null=True, blank=True, related_name="courses")
    languages = models.ManyToManyField("web.Language")
    number_of_lectures = models.PositiveIntegerField()
    mrp_price = models.DecimalField(max_digits=5, decimal_places=2)
    next_session_date = models.DateField(null=True, blank=True)  
    discount_percentage = models.DecimalField(
        max_digits=4,
        decimal_places=1, 
        default=Decimal(0),
        validators=PERCENTAGE_VALIDATOR + [validate_half_or_full_percentage]
    )

    def formatted_discount_percentage(self):
        if self.discount_percentage == self.discount_percentage.to_integral_value():
            return int(self.discount_percentage)
        return float(self.discount_percentage)

    
    @property
    def course_price(self):
        discount_multiplier = Decimal('1') - (self.discount_percentage / Decimal('100'))
        return self.mrp_price * discount_multiplier
    

    def get_similar_courses(self):
        return Course.objects.filter(
            category=self.category 
        ).exclude(id=self.id)[:4]

    def total_decimal_hours(self):
        total_seconds = int(self.total_hours.total_seconds())
        hours, remainder = divmod(total_seconds, 3600)
        minutes, _ = divmod(remainder, 60)
        decimal_hours = hours + minutes / 60
        rounded_hours = round(decimal_hours, 2)
        
        if rounded_hours.is_integer():
            return int(rounded_hours)
        return rounded_hours

    def formatted_price(self):
        if self.mrp_price == self.mrp_price.to_integral_value():
            return int(self.mrp_price)
        return float(self.mrp_price)
    

    def formatted_course_price(self):
        course_price = self.course_price
        rounded_price = course_price.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

        if rounded_price == rounded_price.to_integral_value():
            return int(rounded_price)
        return float(rounded_price)

    
    class Meta:
        db_table="web_Course"
        ordering=["id"]
        verbose_name="course"
        verbose_name_plural="courses"

    def __str__(self):
        return self.title    
    

