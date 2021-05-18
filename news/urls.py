from django.urls import path, include
from news import views
urlpatterns = [
    path('',views.theDailyStar, name='theDailyStar'),
    path('prothomalo',views.prothomAlo, name='prothomalo'),
    path('dhakatribune',views.dhakaTribune, name='dhakatribune'),
    path('bdnews24',views.bdNews24, name='bdnews24')
  
]