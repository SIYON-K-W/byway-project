from django.contrib import admin
from web.models import Category,Course,Language,Author



admin.site.register(Language)


admin.site.register(Category)

class Authoradmin(admin.ModelAdmin):
     list_display=["id","name"]
     search_fields=('name',)

admin.site.register(Author,Authoradmin)


class Courseadmin(admin.ModelAdmin):
    list_display=["id","title","category","rating","formatted_course_price","total_hours"]
    search_fields = ('title', 'author__name')
    autocomplete_fields = ['author']


admin.site.register(Course,Courseadmin)

