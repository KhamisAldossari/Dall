from django.urls import path
from . import views

app_name = "posts"

urlpatterns =[
    path('home', views.post_list, name='post_list'),
    path('add', views.post_create, name='post_create'),

]