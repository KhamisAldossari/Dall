
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from .models import UserProfile
from posts.models import Post
from favorites.models import Favorite
from django.core.mail import send_mail

from django.conf import settings

# Create your views here.

def register_user_view(request: HttpRequest):
    msg = None

    if request.method == "POST":
        try:
            #create a new user
            user = User.objects.create_user(username=request.POST["username"], first_name=request.POST["first_name"], last_name=request.POST["last_name"], email=request.POST["email"], password=request.POST["password"])
            user.save()

            user_profile = UserProfile(user=user)
            user_profile.save()
            login(request,user)
            subject = 'welcome to DALL world'.upper()
            message = f'Hi {user.first_name} {user.last_name}, thank you for registering in dall.'.upper()
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [user.email,]
            send_mail( subject, message, email_from, recipient_list )


            return render(request,"main/welcome_email.html")
            return redirect("accounts:login_user_view")
        except IntegrityError as e:
            msg = f"Please select another username, {e}"
        except Exception as e:
            msg = f"something went wrong {e}"

    return render(request, "accounts/register.html", {"msg" : msg})


def login_user_view(request: HttpRequest):
    msg = None
    if request.method == "POST":
        #first : authenticate the user data
        user = authenticate(request, username=request.POST["username"], password=request.POST["password"])

        if user:
            #second: login the user
            login(request, user)
            return redirect("main:home_view")
        else:
            msg = "Please provide correct username and password"



    return render(request, "accounts/login.html", {"msg" : msg})



def logout_user_view(request: HttpRequest):

    #log out the user
    if request.user.is_authenticated:
        logout(request)    

    return redirect("accounts:login_user_view")



def user_profile_view(request: HttpRequest, user_id):
    msg=None
    try:
    # Use get_object_or_404 for cleaner handling of non-existent objects
        user = get_object_or_404(UserProfile, user__id=user_id)
        user_posts = Post.objects.filter(post_user=user.user)

        # Optimize following list retrieval
        following = [profile.user for profile in UserProfile.objects.all() if user.user in profile.followers.all()]

        # Simplify is_following check
        is_following = user.followers.filter(id=request.user.id).exists()

        followers = user.followers.all()
        number_of_followers = followers.count()
        favorites = Favorite.objects.filter(user=request.user)
            
    except Exception as e :
        msg= f'something went wrong {e}'
        return render(request, 'main/not_found.html',{'msg':msg})
    
    
    return render(request, 'accounts/profile.html', {"user":user,'user_posts':user_posts,'number_of_followers':number_of_followers,"is_following":is_following , 'followers':followers, 'following':following,'favorites':favorites})

def add_follower(request:HttpRequest, user_id):
        
            profile = UserProfile.objects.get(id=user_id)
            profile.followers.add(request.user)
            return redirect('accounts:user_profile_view',user_id=profile.user.id)
        
def remove_follower(request:HttpRequest, user_id):
        
            profile = UserProfile.objects.get(id=user_id)
            profile.followers.remove(request.user)
            return redirect('accounts:user_profile_view',user_id=profile.user.id)

def update_user_view(request: HttpRequest):
    msg = None

    if request.method == "POST":
        try:
            if request.user.is_authenticated:
                user : User = request.user
                user.first_name = request.POST["first_name"]
                user.last_name = request.POST["last_name"]
                user.email = request.POST["email"]
                user.save()

              
                profile = UserProfile.objects.get(user=user)
                
                profile.birth_date = request.POST["birth_date"]
                if 'profile_picture' in request.FILES: profile.profile_picture = request.FILES["profile_picture"]
                profile.bio = request.POST["bio"]
                profile.phone_number = request.POST["phone_number"]
                profile.major = request.POST["major"]
                profile.degree = request.POST["degree"]
                profile.university_name = request.POST["university_name"]

                profile.save()

                return redirect("accounts:user_profile_view", user_id = request.user.id)

            else:
                return redirect("accounts:login_user_view")
        except IntegrityError as e:
            msg = f"Please select another username"
        except Exception as e:
            msg = f"something went wrong {e}"

    return render(request, "accounts/update.html", {"msg" : msg})

