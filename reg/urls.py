from django.urls import path
from . import views

urlpatterns=[
    path('', views.start),
    path('posts', views.show_posts),
    path('registration',views.registr_page),
    path('login',views.loginn)
]