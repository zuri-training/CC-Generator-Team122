from django.urls import path
from .views import home, about_us, contact_us, landingpage, library, profile, documentation, api_ref





urlpatterns = [
    path('', home.as_view(), name='home'),
    path('about_us', about_us.as_view(), name='about_us'),
    path('contact_us', contact_us.as_view(), name='contact_us'),
    path('landingpage', landingpage.as_view(), name='landingpage'),
    path('library', library.as_view(), name='library'),
    path('profile', profile.as_view(), name='profile'),
    path('documentation', documentation.as_view(), name='documentation'),
    path('api_ref', api_ref.as_view(), name='api_ref'),
     ]

