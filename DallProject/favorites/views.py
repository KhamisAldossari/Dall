from django.shortcuts import render ,redirect
from django.http import HttpRequest,HttpResponse
from .models import Favorite
from majors.models import Major
# Create your views here.
def add_favorite_view(request:HttpRequest, major_id):

    if not request.user.is_authenticated:
        return redirect("accounts:login_user_view")

   
    try:

       
        major = Major.objects.get(id=major_id)

        
        user_favored = Favorite.objects.filter(user=request.user, major=major).first() #.first() bring the first Favorite object if exists else None
        
        if not user_favored:
           
            new_favorite = Favorite(user=request.user, major=major)
            new_favorite.save()
        else:
            
            user_favored.delete()

        return redirect("majors:detail_major_view", major_id=major.id)
    except Exception as e:
        return redirect("main:home_view")