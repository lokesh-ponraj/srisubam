from django.urls import path
from . import views

urlpatterns = [
    path('', views.index , name='index'),
    path('home/', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('membership/', views.membership, name='membership'),
    path('matching/', views.matching, name='matching'),
    path('contact/', views.contact, name='contact'),
]
