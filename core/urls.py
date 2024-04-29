from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_user, name='login'),
    path('register/', views.register_user, name='register'),
    path('profile/<int:pk>/', views.user_profile, name='user-profile'),
    path('profile/applications/', views.user_adoption_applications, name='user-adoption-applications'),
    path('profile/applications/withdraw/<int:pk>', views.withdraw_application, name='withdraw-application'),
    path('logout/', views.logout_user, name='logout'),
    path('pets/', views.pets_catalogue, name='pets-catalogue'),
    path('pets/<int:pk>/profile/', views.pet_profile, name='pet-profile'),
    path('pets/<int:pk>/apply/', views.adoption_application, name='pet-apply')
]