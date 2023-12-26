from django.urls import path
from . import views

app_name = "companies"

urlpatterns =[path("add/",views.add_company_view,name="add_company_view"),
              path("update/<company_id>/",views.update_company_view,name="update_company_view"),
              path("delete/<company_id>/",views.delete_company_view,name="delete_company_view"),
              path("home/",views.company_home_view,name="company_home_view"),
              path('detail/<company_id>/',views.detail_company_view,name="detail_company_view"),
              ]