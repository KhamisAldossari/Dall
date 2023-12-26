from django.shortcuts import render, redirect
from django.http import HttpRequest,HttpResponse
from .models import Job

# Create your views here.

def add_job_view(request:HttpRequest):
    msg=None
    try:
        if request.method == "POST":
            new_job= Job(name=request.POST["name"],
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
        view_job=Job.objects.all()
    except:
        return render(request, "main/not_found.html", status=401)
    return render(request , 'jobs/job_home.html',{'view_job':view_job})
def detail_job_view(request:HttpRequest,job_id):
    
    try:
        job_detail=Job.objects.get(id=job_id)
    except:
        return render(request, "main/not_found.html", status=401)
    return render(request, 'jobs/detail_job.html',{"job_detail":job_detail})
    
