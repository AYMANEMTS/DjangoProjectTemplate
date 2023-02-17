from django import forms
from cakeapp import models
from cakeapp.models import Cake




class FormCakeAdmin(forms.ModelForm):
    title = forms.CharField()
    price = forms.CharField()
    descri = forms.CharField()
    cake_img = forms.ImageField()
    
    big_descri = forms.CharField()


    class Meta:
        model = Cake
        fields = ['title','price','descri','cake_img','categorivto','big_descri']