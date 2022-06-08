from django.contrib import admin
from .models import people,address,product,doctor,profile

# Register your models here.
admin.site.register(people)

admin.site.register(address)

admin.site.register(product)

admin.site.register(doctor)

admin.site.register(profile)