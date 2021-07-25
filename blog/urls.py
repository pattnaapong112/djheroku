from blog.views import about, contact, index, persons
from django.urls import path 
from blog.views import index,about,persons,contact

urlpatterns = [
    path('', index),
    path('about/',about),
    path('persons/',persons),
    path('contact/',contact)
   
   
]
