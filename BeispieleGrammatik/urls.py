from django.urls import path
from . import views

app_name='Grammatik'

urlpatterns = [
    path('', views.index, name='index'),
    path('dative', views.PrMitDative, name='dative'),
    path('akk', views.PrMitAkk, name ='akk'),
]
