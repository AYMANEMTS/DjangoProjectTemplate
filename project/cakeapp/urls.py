from django.urls import path
from .views import IndexView,AboutViewPage,MenuView,ServicView,ContactView,SingleCakeView,SingleChefView,Creat

app_name = 'cakeapp'



urlpatterns = [
    path("creat/",Creat.as_view(), name="creat"),   
    path('',IndexView.as_view(),name='index'),
    path('about/',AboutViewPage.as_view(),name='about'),
    path("menu/", MenuView.as_view(), name="menu"),
    path("chef/", ServicView.as_view(), name="chef"),
    path("contact/", ContactView.as_view(), name="contact"),   
    path("<str:slug>/",SingleCakeView.as_view(), name="single"),   
    path("chef/<str:slug>/",SingleChefView.as_view(), name="single-chef"),   
    
]


