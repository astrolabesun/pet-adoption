from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_user, name='login'),
    path('register/', views.register_user, name='register'),
    path('profile/<int:pk>/', views.user_profile, name='user-profile'),
    path('logout/', views.logout_user, name='logout'),
    path('pets/', views.pets_catalogue, name='pets-catalogue')
]