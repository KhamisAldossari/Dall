from django.shortcuts import render, redirect
from django.http import HttpRequest,HttpResponse
from certificates.models import Certificate
from companies.models import Company
from courses.models import Course
from jobs.models import Job
from skills.models import Skill
from .models import Major

# Create your views here.

def add_major_view(request:HttpRequest):
    msg=None
    try:
        if request.method == "POST":
            new_major= Major(name=request.POST["name"],
                                    description=request.POST["description"],
                                    )
            if 'image' in request.FILES:
                new_major.image=request.FILES["image"]

            new_major.save()
            return redirect('majors:majors_home_view')
    except Exception as e:
        msg = f"An error occured, please fill in all fields and try again . {e}"
    return render(request , 'majors/add_major.html',{'msg':msg})

def update_major_view(request:HttpRequest,major_id):
    msg=None
    try:
        update_major=Major.objects.get(id=major_id)
        
        if request.method == "POST":
            update_major.name=request.POST["name"]
            update_major.description=request.POST["description"]
            if 'image' in request.FILES:
                update_major.image=request.FILES["image"]

            update_major.save()
            return redirect ('majors:detail_major_view',major_id=update_major.id)
    except Exception as e:
        msg = f"An error occured, please fill in all fields and try again . {e}"
            
    return render(request, 'majors/update_major.html',{"update_major":update_major,'msg':msg})
def delete_major_view(request:HttpRequest,major_id):
    try:
        delete_major=Major.objects.get(id=major_id)
        '''
        if not request.user == delete_major.owner:
            return render(request, "main/not_authorized.html", status=401)
        '''
        delete_major.delete()
        return redirect('majors:',)
    except Exception as e:
         msg = f"An error occured, please fill in all fields and try again . {e}"
    return render(request, 'majors/detail_major.html',{"msg":msg})
def major_home_view(request:HttpRequest):
    try:
        #view_major=major.objects.all()
        view_major=Major.objects.all()
    except:
        return render(request, "main/not_found.html", status=401)
    return render(request , 'majors/major_home.html',{'view_major':view_major})
def detail_major_view(request:HttpRequest,major_id):
    '''
    try:
        major_detail=Major.objects.get(id=major_id)
        
        comments = Comment.objects.filter(major=major_detail)

        is_favored = request.user.is_authenticated and Favorite.objects.filter(major=major_detail, user=request.user).exists()

        comment_max = Comment.objects.filter(major=major_detail).aggregate(Max("rating"))["rating__max"]
    except:
        return render(request, "main/not_found.html", status=401)
    return render(request, 'major/detail_major.html',{"major_detail":major_detail,'comments':comments,'comment_max':comment_max,"is_favored":is_favored})
    '''
