from django.urls import path
from . import views
from .views import dashboard  # chat

urlpatterns = [    
    path('index/',views.index,name='index'),
    
    path('signup/',views.signup,name='signup'),
    path('',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('department/',views.department,name='department'),

    path('change-password/',views.change_password,name='change-password'),
    path('profile/',views.profile,name='profile'),
    path('forgot-password/',views.forgot_password,name='forgot-password'),
    path('verify-otp/',views.verify_otp,name='verify-otp'),
    path('new-password/',views.new_password,name='new-password'),
   
    path('ajax/validate-email/',views.validate_signup,name='ajax/validate-email'),

     path('dashboard/<int:pk>/', views.dashboard, name='dashboard'), # chat


]
