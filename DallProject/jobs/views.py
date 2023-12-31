from django.shortcuts import render, redirect
from django.http import HttpRequest,HttpResponse
from .models import Job
from majors.models import Major

# Create your views here.

def add_job_view(request:HttpRequest):
    msg=None
    try:
        if request.method == "POST":
            new_job= Job(
            name=request.POST["name"],
            description=request.POST["description"],
            )
            new_job.save()
            return redirect('jobs:job_home_view')
    except Exception as e:
        msg = f"An error occured, please fill in all fields and try again . {e}"
    return render(request , 'jobs/add_job.html',{'msg':msg})

def update_job_view(request:HttpRequest,job_id):
    msg=None
    try:
        update_job=Job.objects.get(id=job_id)
        
        if request.method == "POST":
            update_job.name=request.POST["name"]
            update_job.description=request.POST["description"]

            update_job.save()
            return redirect ('jobs:detail_job_view',job_id=update_job.id)
    except Exception as e:
        msg = f"An error occured, please fill in all fields and try again . {e}"
            
    return render(request, 'jobs/update_job.html',{"update_job":update_job,'msg':msg})
def delete_job_view(request:HttpRequest,job_id):
    try:
        delete_job=Job.objects.get(id=job_id)
        '''
        if not request.user == delete_job.owner:
            return render(request, "main/not_authorized.html", status=401)
        '''
        delete_job.delete()
        return redirect('jobs:',)
    except Exception as e:
         msg = f"An error occured, please fill in all fields and try again . {e}"
    return render(request, 'jobs/detail_job.html',{"msg":msg})

def job_home_view(request:HttpRequest):
    try:
        keyword=None
        if "search" in request.GET:
            keyword =request.GET.get("search")
            view_job = Job.objects.filter(name__contains=keyword)
        else:
            view_job=Job.objects.all()
    except:
        return render(request, "main/not_found.html", status=401)
    return render(request , 'jobs/job_home.html',{'view_job':view_job, 'keyword':keyword})

def detail_job_view(request:HttpRequest,job_id):
    
    try:
        job_detail=Job.objects.get(id=job_id)
    except:
        return render(request, "main/not_found.html", status=401)
    return render(request, 'jobs/detail_job.html',{"job_detail":job_detail})
    
def add_job_major_view(request:HttpRequest, major_id, job_id):

    #if not request.user.has_perm("actors.add_actor"):
        #return render(request, 'main/not_authorized.html')
    
    
    major =Major.objects.get(id=major_id) 
    job = Job.objects.get(id=job_id) 
    major.jobs.add(job) 

    return redirect("majors:detail_major_view", major_id=major_id)

def remove_job_major_view(request:HttpRequest, major_id, job_id):

    #if not request.user.has_perm("actors.add_actor"):
        #return render(request, 'main/not_authorized.html')
    
    
    major =Major.objects.get(id=major_id) 
    job = Job.objects.get(id=job_id) 
    major.jobs.remove(job) 

    return redirect("majors:detail_major_view", major_id=major_id)