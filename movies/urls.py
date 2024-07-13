from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('movies/<int:movie_id>/', views.display_movie, name='display_movie'),
]
