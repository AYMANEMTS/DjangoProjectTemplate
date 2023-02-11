from django.db import models

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
    

    def __str__(self):
        return self.name