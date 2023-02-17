from django.shortcuts import render
from django.views.generic import TemplateView,ListView , DetailView ,CreateView
from .models import Cake,Chef,ContactSms
from .forms import CommandForm,ContactForm,CreatForm
from .models import ComandForminTemplate
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.views.generic import View
from project import settings
from twilio.rest import Client
from django.conf import settings
from django.urls import reverse,reverse_lazy

# Create your views here.


class IndexView(TemplateView):
    template_name = 'pages/index.html'

class AboutViewPage(TemplateView):
    template_name = 'pages/about.html'
    
class MenuView(ListView):
    template_name = 'pages/menu.html'
    model = Cake
    context_object_name = 'contex'

class ContactView(TemplateView):
    model = ContactSms
    form_class = ContactForm
    template_name = 'pages/contact.html'

    def post(self, request, **kwargs):
        name = request.POST.get('name')
        emaltext = request.POST.get('emaltext')
        subject = request.POST.get('subject')                  #this is  methode form in html page
        message = request.POST.get('message')


        ContactSms.objects.create(
            name=name,
            emaltext=emaltext,
            subject=subject,
            message=message,
        )
        return redirect('cake:contact')
    
    

  



class SingleCakeView(DetailView):
    model = Cake
    context_object_name = 'hoho'
    template_name = 'pages/single-cake.html'

    def post(self, request, **kwargs):
        first_name = request.POST.get('firstName')
        last_name = request.POST.get('lastName')
        email = request.POST.get('email')                  #this is  methode form in html page
        phone = request.POST.get('phone')                        #in admin 

        # save the form data to the database
        ComandForminTemplate.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
        )

        return redirect('cake:contact')


class ServicView(ListView):
    model = Chef
    template_name = 'pages/servise.html'
    context_object_name = 'contex'



class SingleChefView(DetailView):
    model = Chef
    context_object_name = 'chef'
    template_name = 'pages/single-chef.html'


    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommandForm()
        return context

    def post(self, request,*args, **kwargs):
        if request.method == 'POST':
            email = request.POST['email']
            phone = request.POST['phone']
            message = request.POST['messag']           #FORM SEND EMAIL

        send_mail(
            email,
            message,
            phone,
            
            [settings.EMAIL_HOST_USER],
            fail_silently=False,
        )        

        return redirect('cake:contact')

        
       
class Creat(CreateView):
    model = Cake
    #fields = ['title','price','descri','cake_img','categorivto','big_descri']
    form_class = CreatForm
    template_name = 'crud/creat.html'
    success_url = reverse_lazy('cake:index')
    