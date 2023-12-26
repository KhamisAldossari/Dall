from django.urls import path
from . import views

app_name = "courses"

urlpatterns =[path("add/",views.add_course_view,name="add_course_view"),
              path("update/<course_id>/",views.update_course_view,name="update_course_view"),
              path("delete/<course_id>/",views.delete_course_view,name="delete_course_view"),
              path("home/",views.course_home_view,name="course_home_view"),
              path('detail/<course_id>/',views.detail_course_view,name="detail_course_view"),
              ]