from django.shortcuts import render,redirect

from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView,FormView
from django.urls import reverse,reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import RegisterForm

from django.contrib.auth import login
# Create your views here.

class Profile(LoginRequiredMixin, TemplateView):
    template_name = 'user/profile.html'
    login_url = 'auth:login'


class Home(TemplateView):
    template_name = 'user/home.html'



class LoogIn(LoginView):
    redirect_authenticated_user = False
    template_name = 'user/login.html'

    def get_success_url(self):
        messages.info(self.request,'welcom to your profile')
        return reverse_lazy('auth:profile')

    def form_invalid(self, form):
        messages.error(self.request,'ghalat awld lklba')
        return self.render_to_response(self.get_context_data(form=form))



class Register(FormView):
    redirect_authenticated_user = True
    template_name = 'user/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('auth:profile')
    

    def dispatch(self,request,*args,**kwargs):
        if request.user.is_authenticated:
           return redirect('auth:profile')
        

    def form_valid(self, form):
        user = form.save()
        if user:
            login(self.request,user)
        return redirect(self.success_url)

