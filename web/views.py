from django.shortcuts import render,get_object_or_404
from django.db.models import Count
from web.models import Course as Coursemodel, Category

def Home(request):
    courses = Coursemodel.objects.all().order_by('-rating', '-rated_customers_count')[:4]
    categories = Category.objects.annotate(total_courses=Count('courses'))

    context = {
        "login": False,
        "courses": courses,
        "categories": categories
    }
    return render(request, "index.html", context=context)


def Course(request,pk):
    course_content=get_object_or_404(Coursemodel.objects.filter(pk=pk))
    similar_courses = course_content.get_similar_courses()
    context={
        "login":True,
        "course":course_content,
        "similar_courses":similar_courses
    }
    return render(request,"singlepage.html",context=context)


def Courses(request,category):
    if(category=="all"):
        courses_list= Coursemodel.objects.all().order_by('-rating', '-rated_customers_count')
    else:    
       courses_list = Coursemodel.objects.filter(category__name=category)
    print(courses_list)
    context={
        "login":True,
        "courses":courses_list,
        "slug":category
    }
    return render(request,"courses.html",context=context)