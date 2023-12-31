from django.urls import path
from . import views

app_name = "favorites"

urlpatterns =[
    path('<major_id>/add/', views.add_favorite_view, name="add_favorite_view"),
    ]