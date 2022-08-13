from django.urls import path
from . import views
from django.contrib import admin
from .views import (tutorialpreference)



urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('logout_req', views.logout_req, name='logout_req'),
    path('<int:tutorialid>/tutorialpreference/<int:tutorialpreference>/', views.tutorialpreference, name='tutorialpreference'),
#     path('<int:tutorialid>/cardpreference/<int:cardpreference>/', views.cardpreference, name='cardpreference'),
]
