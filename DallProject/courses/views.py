from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpRequest,HttpResponse
from .models import Course
from majors.models import Major

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
            update_course.duration=request.POST["duration"]
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
        return redirect('courses:course_home_view')
    except Exception as e:
         msg = f"An error occured, please fill in all fields and try again . {e}"
    return render(request, 'courses/detail_course.html',{"msg":msg})
def course_home_view(request:HttpRequest):
    try:
        keyword=None
        if "search" in request.GET:
            keyword =request.GET.get("search")
            view_course = Course.objects.filter(name__contains=keyword)
        else:
        #view_course=course.objects.all()
            view_course=Course.objects.all()
    except:
        return render(request, "main/not_found.html", status=401)
    return render(request , 'courses/course_home.html',{'view_course':view_course , 'keyword':keyword})
def detail_course_view(request:HttpRequest,course_id):
    
    try:
        course_detail=Course.objects.get(id=course_id)
    except:
        return render(request, "main/not_found.html", status=401)
    return render(request, 'courses/detail_course.html',{"course_detail":course_detail})
    
def add_course_major_view(request:HttpRequest, major_id, course_id):

    #if not request.user.has_perm("actors.add_actor"):
        #return render(request, 'main/not_authorized.html')
    
    
    major =Major.objects.get(id=major_id) 
    course = Course.objects.get(id=course_id) 
    major.courses.add(course) 

    return redirect("majors:detail_major_view", major_id=major_id)

def remove_course_major_view(request:HttpRequest, major_id, course_id):

    #if not request.user.has_perm("actors.add_actor"):
        #return render(request, 'main/not_authorized.html')
    
    
    major =Major.objects.get(id=major_id) 
    course = Course.objects.get(id=course_id) 
    major.courses.remove(course) 

    return redirect("majors:detail_major_view", major_id=major_id)