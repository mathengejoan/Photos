from django.urls import path,include
from . import views

app_name = 'oreo'
urlpatterns =[

    path('', views.index, name='index'),
    path('add_images', views.add_images, name='add_images'),
]