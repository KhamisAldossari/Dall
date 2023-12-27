from django.urls import path
from . import views

app_name = "skills"

urlpatterns =[path("add/",views.add_skill_view,name="add_skill_view"),
              path("update/<skill_id>/",views.update_skill_view,name="update_skill_view"),
              path("delete/<skill_id>/",views.delete_skill_view,name="delete_skill_view"),
              path("home/",views.skill_home_view,name="skill_home_view"),
              path('detail/<skill_id>/',views.detail_skill_view,name="detail_skill_view"),
              path("add/<major_id>/<skill_id>/", views.add_skill_major_view, name="add_skill_major_view"),
              path("remove/<major_id>/<skill_id>/", views.remove_skill_major_view, name="remove_skill_major_view"),
              ]