from django.urls import path
from startdownload import view

urlpatterns = [
   path('download/', views.download_card, name='download')
]