from django.shortcuts import render, redirect
from django.http import HttpRequest,HttpResponse
from courses.models import Course
from jobs.models import Job
from skills.models import Skill
from .models import Company

# Create your views here.

def add_company_view(request:HttpRequest):
    msg=None
    try:
        if request.method == "POST":
            new_company= Company(name=request.POST["name"],
                                    description=request.POST["description"],
                                    industry=request.POST["industry"],
                                    )
            if 'company_image' in request.FILES:
                new_company.company_image=request.FILES["company_image"]

            new_company.save()
            return redirect('companies:company_home_view')
    except Exception as e:
        msg = f"An error occured, please fill in all fields and try again . {e}"
    return render(request , 'companies/add_company.html',{'msg':msg})

def update_company_view(request:HttpRequest,company_id):
    msg=None
    try:
        update_company=Company.objects.get(id=company_id)
        
        if request.method == "POST":
            update_company.name=request.POST["name"]
            update_company.description=request.POST["description"]
            update_company.industry=request.POST["industry"]
            if 'company_image' in request.FILES:
                update_company.company_image=request.FILES["company_image"]

            update_company.save()
            return redirect ('companies:detail_company_view',company_id=update_company.id)
    except Exception as e:
        msg = f"An error occured, please fill in all fields and try again . {e}"
            
    return render(request, 'companies/update_company.html',{"update_company":update_company,'msg':msg})
def delete_company_view(request:HttpRequest,company_id):
    try:
        delete_company=Company.objects.get(id=company_id)
        '''
        if not request.user == delete_company.owner:
            return render(request, "main/not_authorized.html", status=401)
        '''
        delete_company.delete()
        return redirect('companies:company_home_view')
    except Exception as e:
         msg = f"An error occured, please fill in all fields and try again . {e}"
    return render(request, 'companies/detail_company.html',{"msg":msg})
def company_home_view(request:HttpRequest):
    try:
        #view_company=company.objects.all()
        view_company=Company.objects.all()
    except:
        return render(request, "main/not_found.html", status=401)
    return render(request , 'companies/company_home.html',{'view_company':view_company})
def detail_company_view(request:HttpRequest,company_id):
    
    try:
        company_detail=Company.objects.get(id=company_id)
    except:
        return render(request, "main/not_found.html", status=401)
    return render(request, 'companies/detail_company.html',{"company_detail":company_detail})
    
