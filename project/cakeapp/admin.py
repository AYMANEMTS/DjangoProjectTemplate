from django.contrib import admin
from .models import Cake,Chef,ComandForminTemplate,ContactCheFform,ContactSms
from user_auth.models import Profile
# Register your models here.


admin.site.register(Cake)
admin.site.register(Chef)
admin.site.register(ComandForminTemplate)
admin.site.register(ContactCheFform)
admin.site.register(ContactSms)
admin.site.register(Profile)
