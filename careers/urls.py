from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name='index'),
    path('about/',aboutme,name='about'),
    path('contact/',contact,name='contact'),
    path('services/',services,name='services'),
    path('job-listings/',joblisting,name='job-listings'),
]