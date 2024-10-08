# Generated by Django 5.1.1 on 2024-09-06 04:50

import django.core.validators
import django.db.models.deletion
import web.models
from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('profile_image', models.FileField(upload_to='course/authors/')),
            ],
            options={
                'verbose_name': 'Author',
                'verbose_name_plural': 'Authors',
                'db_table': 'web_Author',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('logo', models.FileField(upload_to='category/icons/')),
            ],
            options={
                'verbose_name': 'course_category',
                'verbose_name_plural': 'course_categories',
                'db_table': 'web_Category',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'course_Language',
                'verbose_name_plural': 'course_Languages',
                'db_table': 'web_Language',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('card_title', models.CharField(max_length=28)),
                ('image', models.ImageField(upload_to='course/images/')),
                ('thumbnail_image', models.ImageField(upload_to='course/thumbnailimages/')),
                ('description', models.TextField()),
                ('rating', models.FloatField(validators=[django.core.validators.MinValueValidator(1.0), django.core.validators.MaxValueValidator(5.0)])),
                ('rated_customers_count', models.PositiveIntegerField(default=0)),
                ('total_hours', models.DurationField()),
                ('number_of_lectures', models.PositiveIntegerField()),
                ('mrp_price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('next_session_date', models.DateField(blank=True, null=True)),
                ('discount_percentage', models.DecimalField(decimal_places=1, default=Decimal('0'), max_digits=4, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100), web.models.validate_half_or_full_percentage])),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='web.author')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='courses', to='web.category')),
                ('languages', models.ManyToManyField(to='web.language')),
            ],
            options={
                'verbose_name': 'course',
                'verbose_name_plural': 'courses',
                'db_table': 'web_Course',
                'ordering': ['id'],
            },
        ),
    ]
