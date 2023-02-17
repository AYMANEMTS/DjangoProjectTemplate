from django.shortcuts import render
from cakeapp.models import Cake
from .forms import FormCakeAdmin
from django.views.generic import ListView , DetailView ,CreateView , DeleteView , UpdateView
from django.urls import reverse , reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
# Create your views here.

class ModerList(LoginRequiredMixin,ListView):
    model = Cake
    template_name = 'moder/list.html'
    context_object_name = 'context'

class ModerDetail(LoginRequiredMixin,DetailView):
    model = Cake
    template_name = 'moder/detail.html'
    form_class = FormCakeAdmin


class Creat(LoginRequiredMixin,CreateView):
    model = Cake                                                    
    template_name = 'moder/creat.html'
    form_class = FormCakeAdmin
    success_url = reverse_lazy('my_admin:list')

class Update(LoginRequiredMixin,UpdateView):
    model = Cake
    template_name = 'moder/update.html'
    form_class = FormCakeAdmin
    success_url = reverse_lazy('my_admin:list')

class Delet(LoginRequiredMixin,DeleteView):
    model = Cake
    template_name = 'moder/delet.html'
    success_url = reverse_lazy('my_admin:list')

class Mylogin(LoginView):
    redirect_authenticated_user = False
    template_name = 'moder/login.html'

    def get_success_url(self):
        return reverse_lazy('list')

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))
