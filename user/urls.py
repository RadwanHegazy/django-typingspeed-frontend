from django.urls import path
from .auth import login, register, profile, logout


urlpatterns = [
    path('auth/login/',login.login_view.as_view(),name='login'),
    path('auth/register/',register.register_view.as_view(),name='register'),
    path('auth/logout/',logout.logout_view.as_view(),name='logout'),
    path('',profile.profile_view.as_view(),name='profile'),
]