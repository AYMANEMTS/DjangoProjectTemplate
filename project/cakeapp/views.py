from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from .models import Cake
# Create your views here.


class IndexView(TemplateView):
    template_name = 'pages/index.html'

class AboutViewPage(TemplateView):
    template_name = 'pages/about.html'
    
class MenuView(ListView):
    template_name = 'pages/menu.html'
    model = Cake
    queryset = Cake.objects.all()
    context_object_name = 'contex'

class ServicView(TemplateView):
    template_name = 'pages/servise.html'

class ContactView(TemplateView):
    template_name = 'pages/contact.html'