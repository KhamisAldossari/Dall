from django.shortcuts import render, redirect
from django.http import HttpRequest,HttpResponse
from companies.models import Company
from courses.models import Course
from jobs.models import Job
from skills.models import Skill
from .models import Certificate
from majors.models import Major

# Create your views here.

def add_certificate_view(request:HttpRequest):
    msg=None
    try:
        if request.method == "POST":
            new_certificate= Certificate(name=request.POST["name"],
                                    description=request.POST["description"],
                                    provider=request.POST["provider"],
                                    )
            if 'certificate_image' in request.FILES:
                new_certificate.certificate_image=request.FILES["certificate_image"]

            new_certificate.save()
            return redirect('certificates:certificate_home_view')
    except Exception as e:
        msg = f"An error occured, please fill in all fields and try again . {e}"
    return render(request , 'certificates/add_certificate.html',{'msg':msg})

def update_certificate_view(request:HttpRequest,certificate_id):
    msg=None
    try:
        update_certificate=Certificate.objects.get(id=certificate_id)
        
        if request.method == "POST":
            update_certificate.name=request.POST["name"]
            update_certificate.description=request.POST["description"]
            update_certificate.provider=request.POST["provider"]
            if 'certificate_image' in request.FILES:
                update_certificate.certificate_image=request.FILES["certificate_image"]

            update_certificate.save()
            return redirect ('certificates:detail_certificate_view',certificate_id=update_certificate.id)
    except Exception as e:
        msg = f"An error occured, please fill in all fields and try again . {e}"
            
    return render(request, 'certificates/update_certificate.html',{"update_certificate":update_certificate,'msg':msg})
def delete_certificate_view(request:HttpRequest,certificate_id):
    try:
        delete_certificate=Certificate.objects.get(id=certificate_id)
        '''
        if not request.user == delete_certificate.owner:
            return render(request, "main/not_authorized.html", status=401)
        '''
        delete_certificate.delete()
        return redirect('certificates:certificate_home_view')
    except Exception as e:
         msg = f"An error occured, please fill in all fields and try again . {e}"
    return render(request, 'certificates/detail_certificate.html',{"msg":msg})
def certificate_home_view(request:HttpRequest):
    try:
        if "search" in request.GET:
            keyword =request.GET.get("search")
            view_certificate = Certificate.objects.filter(name__contains=keyword)
        else:
            #view_certificate=certificate.objects.all()
            view_certificate=Certificate.objects.all()
    except:
        return render(request, "main/not_found.html", status=401)
    return render(request , 'certificates/certificate_home.html',{'view_certificate':view_certificate})
def detail_certificate_view(request:HttpRequest,certificate_id):
    
    try:
        certificate_detail=Certificate.objects.get(id=certificate_id)
    except:
        return render(request, "main/not_found.html", status=401)
    return render(request, 'certificates/detail_certificate.html',{"certificate_detail":certificate_detail})
    
def add_certificate_major_view(request:HttpRequest, major_id, certificate_id):

    #if not request.user.has_perm("actors.add_actor"):
        #return render(request, 'main/not_authorized.html')
    
    
    major =Major.objects.get(id=major_id) 
    certificate = Certificate.objects.get(id=certificate_id) 
    major.certificates.add(certificate) 

    return redirect("majors:detail_major_view", major_id=major_id)

def remove_certificate_major_view(request:HttpRequest, major_id, certificate_id):

    #if not request.user.has_perm("actors.add_actor"):
        #return render(request, 'main/not_authorized.html')
    
    
    major =Major.objects.get(id=major_id) 
    certificate = Certificate.objects.get(id=certificate_id) 
    major.certificates.remove(certificate) 

    return redirect("majors:detail_major_view", major_id=major_id)