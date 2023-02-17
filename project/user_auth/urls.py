from django.urls import path
from .views import Profile,Home,LoogIn,Register
from django.contrib.auth.views import LogoutView


app_name = 'user_auth'


urlpatterns = [    
    path('',Home.as_view(),name='home'),
    path('login/',LoogIn.as_view(),name='login'),
    path('register/',Register.as_view(),name='register'),
    path('profile/',Profile.as_view(),name='profile'),   
    path('logout/',LogoutView.as_view(next_page='home'),name="logout"),
]
