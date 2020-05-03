from django.urls import path
from .views import home,wth

urlpatterns=[
    path('',home,name='home'),
    path('wth',wth,name='wth')
]