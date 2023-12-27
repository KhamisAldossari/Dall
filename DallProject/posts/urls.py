from django.urls import path
from . import views

app_name = "posts"

urlpatterns =[
    path('home', views.post_list, name='post_list'),
    path('add', views.post_create, name='post_create'),
    path('detail/<post_id>/', views.post_detail, name='post_detail'),
    path('update/<post_id>/', views.post_update, name='post_update'),
]