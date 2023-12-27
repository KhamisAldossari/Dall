from django.urls import path
from . import views

app_name = "majors"

urlpatterns =[path("add/",views.add_major_view,name="add_major_view"),
              path("update/<major_id>/",views.update_major_view,name="update_major_view"),
              path("delete/<major_id>/",views.delete_major_view,name="delete_major_view"),
              path("home/",views.major_home_view,name="major_home_view"),
              path("detail/<major_id>/",views.detail_major_view,name="detail_major_view")
              ]