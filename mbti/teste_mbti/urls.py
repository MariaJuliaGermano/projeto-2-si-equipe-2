from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('results/', views.results, name='results'),
    path('equipe/', views.equipe, name='equipe'),
    path('tiposPersonalidades', views.tiposPersonalidades, name='tipos'),
]