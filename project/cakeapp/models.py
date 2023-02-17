from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from requests import request
import os
from twilio.rest import Client

cate = (
    ('BIRTHDAY','BIRTHDAY'),
    ('WEDDING','WEDDING'),
    ('CUSTOM','CUSTOM'),  

)



class Cake(models.Model):
    title = models.CharField(max_length=50,blank=False,null=True)
    price = models.DecimalField(max_digits=5,decimal_places=2,null=True,blank=True)
    descri = models.TextField(max_length=1000,null=True,blank=True)
    cake_img = models.ImageField(upload_to='imgs_cake/',null=True,blank=True)
    #categori = models.ForeignKey('Qatego',on_delete=models.CASCADE,null=True,blank=True)
    categorivto = models.CharField(max_length=50,choices=cate,null=True,blank=True)
    big_descri = RichTextField(null=True,blank=True)
    slug = models.SlugField(null=True,blank=True)


    def save(self,*args, **kwargs):
        self.slug = slugify(self.title)
        super(Cake,self).save(*args, **kwargs)

    def __str__(self):
        return self.title


#class Qatego(models.Model):
    #name = models.CharField(max_length=50,null=True,blank=True)


    #def  __str__(self):
        #return self.name


class Chef(models.Model):
    name = models.CharField(max_length=50,null=False,blank=True)
    spes = models.TextField(max_length=300,null=True,blank=True)
    chef_img = models.ImageField(upload_to='imgs_chef/',null=True,blank=True)
    slug = models.SlugField(null=True,blank=True)
    


    def save(self,*args, **kwargs):
        self.slug = slugify(self.name)
        super(Chef,self).save(*args, **kwargs)
    

    def __str__(self):
        return self.name


class ComandForminTemplate(models.Model):
    first_name = models.CharField(max_length=50,null=True,blank=True)
    last_name = models.CharField(max_length=50,null=True,blank=True)
    email = models.CharField(max_length=100,null=True,blank=True)
    phone = models.CharField(max_length=15,null=True,blank=True)
    #cake = models.OneToOneField(Cake,on_delete=models.CASCADE)

    
    def __str__(self):
        return self.phone



class ContactCheFform(models.Model):
    first = models.CharField(max_length=50)
    last = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.IntegerField()
    mess = models.TextField(max_length=500,null=True,blank=True)

    class Meta:
        verbose_name = 'Contact Chef'
        verbose_name_plural = 'Contact Form'


    def __str__(self):
        return self.email


class ContactSms(models.Model):
    name = models.CharField(max_length=50)
    emaltext = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    message = models.CharField(max_length=100)

    def __str__(self):
        return self.name


