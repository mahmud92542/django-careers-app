from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name='index'),
    path('job-listings/',joblisting,name='job-listings'),
    path('about',aboutme,name='about'),
]