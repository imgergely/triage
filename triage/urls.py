from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_login, name='app-login'),
    path('home/', views.home, name='app-home'),
    path('logout/', views.user_logout, name='app-logout'),
    
]
