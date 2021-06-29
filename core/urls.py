from django.urls import path
from .views import home,weather

urlpatterns=[
    path('',home,name='home'),
    path('weather',weather,name='weather')
]