from django.urls import path
from . import views

app_name = "certificates"

urlpatterns =[path("add/",views.add_certificate_view,name="add_certificate_view"),
              path("update/<certificate_id>/",views.update_certificate_view,name="update_certificate_view"),
              path("delete/<certificate_id>/",views.delete_certificate_view,name="delete_certificate_view"),
              path("home/",views.certificate_home_view,name="certificate_home_view"),
              ]