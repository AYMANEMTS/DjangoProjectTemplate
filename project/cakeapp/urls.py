from django.urls import path
from .views import IndexView,AboutViewPage,MenuView,ServicView,ContactView

urlpatterns = [
    path('',IndexView.as_view(),name='index'),
    path('about/',AboutViewPage.as_view(),name='about'),
    path("menu/", MenuView.as_view(), name="menu"),
    path("servic/", ServicView.as_view(), name="servic"),
    path("contact/", ContactView.as_view(), name="contact")   
]
