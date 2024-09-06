from django.urls import path
from web.views import Home,Course,Courses


app_name = "web"


urlpatterns = [
    path('',Home,name="homepage"),
    path('course/<int:pk>',Course,name="coursepage"),
    path('courses/<str:category>',Courses,name="coursespage"),
]