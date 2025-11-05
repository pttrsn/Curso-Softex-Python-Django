from django.urls import path
from . import views # O '.' importa as 'views' do app atual

urlpatterns = [
    path('home', views.home, name='home'),
]
