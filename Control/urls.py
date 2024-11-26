from django.urls import path
from . import views

urlpatterns = [
    path('control/', views.Control_page),
    path('getdata/', views.get_data),
    path('26/on/', views.LED1_ON),
    path('26/off/', views.LED1_OFF),
    path('27/on/', views.LED2_ON),
    path('27/off/', views.LED2_OFF),
]