from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpRequest,HttpResponse
from companies.models import Company
from jobs.models import Job
from skills.models import Skill
from .models import Course

# Create your views here.

def add_course_view(request:HttpRequest):
    msg=None
    try:
        if request.method == "POST":
            new_course= Course(name=request.POST["name"],
                                    description=request.POST["description"],
                                    provider=request.POST["provider"],
                                    duration=request.POST["duration"],
                                    )
            if 'course_image' in request.FILES:
                new_course.course_image=request.FILES["course_image"]

            new_course.save()
            return redirect('courses:course_home_view')
    except Exception as e:
        msg = f"An error occured, please fill in all fields and try again . {e}"
    return render(request , 'courses/add_course.html',{'msg':msg})

def update_course_view(request:HttpRequest,course_id):
    msg=None
    try:
        update_course=Course.objects.get(id=course_id)
        
        if request.method == "POST":
            update_course.name=request.POST["name"]
            update_course.description=request.POST["description"]
            update_course.provider=request.POST["provider"]
            update_course.duration=request["duration"]
            if 'course_image' in request.FILES:
                update_course.course_image=request.FILES["course_image"]

            update_course.save()
            return redirect ('courses:detail_course_view',course_id=update_course.id)
    except Exception as e:
        msg = f"An error occured, please fill in all fields and try again . {e}"
            
    return render(request, 'courses/update_course.html',{"update_course":update_course,'msg':msg})
def delete_course_view(request:HttpRequest,course_id):
    try:
        delete_course=Course.objects.get(id=course_id)
        '''
        if not request.user == delete_course.owner:
            return render(request, "main/not_authorized.html", status=401)
        '''
        delete_course.delete()
        return redirect('courses:',)
    except Exception as e:
         msg = f"An error occured, please fill in all fields and try again . {e}"
    return render(request, 'courses/detail_course.html',{"msg":msg})
def course_home_view(request:HttpRequest):
    try:
        #view_course=course.objects.all()
        view_course=Course.objects.all()
    except:
        return render(request, "main/not_found.html", status=401)
    return render(request , 'courses/course_home.html',{'view_course':view_course})