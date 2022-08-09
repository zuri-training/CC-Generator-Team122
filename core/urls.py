from django.urls import path
from .views import home, about_us





urlpatterns = [
    path('', home.as_view(), name='home'),
    path('about_us', about_us.as_view(), name='about_us')
    # path('contact_us', views.contact_us, name='contact_us')
    # path('library', views.library, name='library')
    # path('profile', profile, name='profile')
    # path('settings', view.settings, name='settings')
    # path('documentation', view.documentation, name='documentation')
    # path('api_ref', view.api_ref, name='api_ref')
     ]

