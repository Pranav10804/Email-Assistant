from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('submit/', views.submit, name='submit'),
    path('classify/', views.classify, name='classify'),
    path('submit1/', views.submit1, name='submit'),
    path('summarise/', views.summarise, name='summarise'),

]