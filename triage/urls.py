from django.urls import path
from . import views
from .views import TriageDetail
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', views.user_login, name='app-login'),
    path('home/', views.home, name='app-home'), 
    path('under_treatment/', views.get_under_treatment, name='under_treatment'),
    path('set_under_treatment/', views.set_under_treatment, name='set_under_treatment'),
    path('<int:pk>/', login_required(TriageDetail.as_view()), name='triage_detail'),
    path('triage_form/', views.triage, name='app-new_triage_form'),
    path('logout/', views.user_logout, name='app-logout'),
    
]
