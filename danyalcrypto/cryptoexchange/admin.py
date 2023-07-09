from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Customer)
admin.site.register(Coin)
admin.site.register(Order)
admin.site.register(Stock)