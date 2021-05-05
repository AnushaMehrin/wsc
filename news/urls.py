from django.urls import path, include
from news import views
urlpatterns = [
    path('home', views.home, name='home'),
    path('dhakatribune',views.dhakaTribune, name='index'),
    path('prothomalo',views.prothomAlo, name='index'),
    path('bdnews24',views.bdNews24, name='index')
  
]