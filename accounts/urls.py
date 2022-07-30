from django.urls import path
from . import views

app_name = "accounts"
urlpatterns = [
    path('', views.home_view, name="homepage"),
    # path('explore/', views.explore, name="explore"),
    path('signup/', views.signup_view, name="signup"),
    path('login/', views.login_view, name="login"),
]
