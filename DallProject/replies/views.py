from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from replies.models import Reply
# Create your views here.

def add_reply(request, post_id):
    msg=None
    try:
        if request.method == "POST":
            new_reply=Reply(
            title=request.POST["title"],
            content=request.POST["content"],
            reply_user=request.user,
            post=Post.objects.get(id=post_id),
            )
            new_reply.save()
            return redirect('posts:post_detail',post_id)
    except Exception as e:
        msg = f"An error occured, please fill in all fields and try again . {e}"
        return render(request , 'main/not_found.html',{'msg':msg})
