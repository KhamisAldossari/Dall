from django.urls import path
from . import views

app_name = "replies"

urlpatterns =[
        path('add/<post_id>', views.add_reply, name='add_reply'),
]