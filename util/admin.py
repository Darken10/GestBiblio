from django.contrib import admin
from .models import Admin,Bibliothecaire,Visiteur

# Register your models here.


admin.site.register(Admin)
admin.site.register(Bibliothecaire)
admin.site.register(Visiteur)