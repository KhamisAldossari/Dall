from django.shortcuts import render, redirect
from django.http import HttpRequest,HttpResponse
from .models import Skill
from majors.models import Major

# Create your views here.

def add_skill_view(request:HttpRequest):
    msg=None
    try:
        if request.method == "POST":
            new_skill= Skill(name=request.POST["name"])
            new_skill.save()
            return redirect('skills:skill_home_view')
    except Exception as e:
        msg = f"An error occured, please fill in all fields and try again . {e}"
    return render(request , 'skills/add_skill.html',{'msg':msg})

def update_skill_view(request:HttpRequest,skill_id):
    msg=None
    try:
        update_skill=Skill.objects.get(id=skill_id)
        
        if request.method == "POST":
            update_skill.name=request.POST["name"]
            update_skill.save()
            return redirect ('skills:detail_skill_view',skill_id=update_skill.id)
    except Exception as e:
        msg = f"An error occured, please fill in all fields and try again . {e}"
            
    return render(request, 'skills/update_skill.html',{"update_skill":update_skill,'msg':msg})
def delete_skill_view(request:HttpRequest,skill_id):
    try:
        delete_skill=Skill.objects.get(id=skill_id)
        '''
        if not request.user == delete_skill.owner:
            return render(request, "main/not_authorized.html", status=401)
        '''
        delete_skill.delete()
        return redirect('skills:skill_home_view')
    except Exception as e:
         msg = f"An error occured, please fill in all fields and try again . {e}"
    return render(request, 'skills/detail_skill.html',{"msg":msg})
def skill_home_view(request:HttpRequest):
    try:
        if "search" in request.GET:
            keyword =request.GET.get("search")
            view_skill = Skill.objects.filter(name__contains=keyword)
        else:
            view_skill=Skill.objects.all()
    except:
        return render(request, "main/not_found.html", status=401)
    return render(request , 'skills/skill_home.html',{'view_skill':view_skill})
def detail_skill_view(request:HttpRequest,skill_id):
    
    try:
        skill_detail=Skill.objects.get(id=skill_id)
    except:
        return render(request, "main/not_found.html", status=401)
    return render(request, 'skills/detail_skill.html',{"skill_detail":skill_detail})

def add_skill_major_view(request:HttpRequest, major_id, skill_id):

    #if not request.user.has_perm("actors.add_actor"):
        #return render(request, 'main/not_authorized.html')
    
    
    major =Major.objects.get(id=major_id) 
    skill = Skill.objects.get(id=skill_id) 
    major.skills.add(skill) 

    return redirect("majors:detail_major_view", major_id=major_id)

def remove_skill_major_view(request:HttpRequest, major_id, skill_id):

    #if not request.user.has_perm("actors.add_actor"):
        #return render(request, 'main/not_authorized.html')
    
    
    major =Major.objects.get(id=major_id) 
    skill = Skill.objects.get(id=skill_id) 
    major.skills.remove(skill) 

    return redirect("majors:detail_major_view", major_id=major_id)
    
