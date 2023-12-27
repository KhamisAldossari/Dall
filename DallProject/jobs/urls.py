from django.urls import path
from . import views

app_name = "jobs"

urlpatterns =[path("add/",views.add_job_view,name="add_job_view"),
              path("update/<job_id>/",views.update_job_view,name="update_job_view"),
              path("delete/<job_id>/",views.delete_job_view,name="delete_job_view"),
              path("home/",views.job_home_view,name="job_home_view"),
              path('detail/<job_id>/',views.detail_job_view,name="detail_job_view"),
              path("add/<major_id>/<job_id>/", views.add_job_major_view, name="add_job_major_view"),
              path("remove/<major_id>/<job_id>/", views.remove_job_major_view, name="remove_job_major_view"),
              ]