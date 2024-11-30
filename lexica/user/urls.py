from django.urls import path
from .views import RegisterView, LoginView, ProfileView, home

urlpatterns = [
    path('', home, name='home'),  # Home view
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
]
