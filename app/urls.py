from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('projs/', views.proj_view, name='projects'),
    path('about/<int:pid>', views.about_view, name='about'),
]
