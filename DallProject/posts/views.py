from django.shortcuts import render, redirect
from .models import Post
from replies.models import Reply
# Create your views here.


def post_list(request):
    try:
        if "search" in request.GET:
            posts = Post.objects.filter(title__contains=request.GET["search"])
        elif "category" in request.GET:
            posts = Post.objects.filter(category=request.GET["category"])
        else:
            posts = Post.objects.all()
        
        return render(request, 'posts/post_list.html', {'posts': posts})
    except Exception as e:
        return render(request, 'main/not_found.html')

def post_create(request):
    msg=None
    try:
        if request.method == "POST":
            new_post=Post(
            title=request.POST["title"],
            content=request.POST["content"],
            post_user=request.user,
            )
            new_post.save()
            return redirect('posts:post_list')
    except Exception as e:
        msg = f"An error occured, please fill in all fields and try again . {e}"
    return render(request , 'posts/post_create.html',{'msg':msg})

def post_detail(request, post_id):
    msg=None
    try:  
        post= Post.objects.get(id=post_id)
        replies= post.reply_set.all()
    except Exception as e:
        msg= f"An error occured ! ({e})"
        return render(request, 'main/not_found.html',{'msg':msg})

    return render(request, 'posts/post_detail.html', {'post': post, "replies":replies})


