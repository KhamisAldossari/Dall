from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("register/", views.register_user_view, name="register_user_view"),
    path("login/", views.login_user_view, name="login_user_view"),
    path("logout/", views.logout_user_view, name="logout_user_view"),
    path("profile/<user_id>/", views.user_profile_view, name="user_profile_view"),
    path("update/", views.update_user_view, name="update_user_view"),
    path('followers/add/<user_id>/', views.add_follower, name='add_follower'),
    path('followers/remove/<user_id>/', views.remove_follower, name='remove_follower'),
    
    
   
]