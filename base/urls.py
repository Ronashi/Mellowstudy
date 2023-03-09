from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('room/<str:pk>/', views.room, name="room" ),
]


# /home/mellow/Desktop/CODERIG/DJANGO/Mellowstudy/Mellowstudy/templates/home.html