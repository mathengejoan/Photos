from django.urls import path,include
from . import views

app_name = 'oreo'
urlpatterns =[
    path('', views.index, name='index'),
    path('add_album', views.add_album, name='add_album'),
    path('(?P<album_id>[0-9]+/)', views.details, name='details'),

]