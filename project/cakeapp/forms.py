from django import forms
from . import models
from .models import ComandForminTemplate,ContactSms,Cake

class CommandForm(forms.Form):
  class Meta:
      model = ComandForminTemplate
      fields = '__all__'


class ContactForm(forms.ModelForm):
    name = forms.CharField(widget = forms.TextInput (attrs={"class":"form-control","placeholder":"name"}))
    emaltext = forms.CharField(widget = forms.TextInput (attrs={"class":"form-control","placeholder":"email"}))
    subject = forms.CharField(widget = forms.TextInput (attrs={"class":"form-control","placeholder":"subject"}))
    message = forms.CharField(widget = forms.Textarea (attrs={"class":"form-control","placeholder":"message"}))

    class Meta:
      model = ContactSms
      fields = ['name','emaltext','subject','message']



class CreatForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput)
    price = forms.DecimalField(widget=forms.NumberInput)
    descri = forms.CharField(widget=forms.TextInput)
    cake_img = forms.ImageField()
    #categori = forms.ForeignKey('Qatego',on_delete=forms.CASCADE,null=True,blank=True)
    categorivto = forms.ChoiceField(choices=models.cate)
    big_descri = forms.CharField(widget=forms.Textarea)
    #slug = forms.SlugField()
    

    class Meta:
      model = Cake
      fields = ['title','price','descri','cake_img','categorivto','big_descri']