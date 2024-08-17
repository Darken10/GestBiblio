from django.contrib import admin
from django.contrib.auth.models import User
from util.models import Bibliothecaire
from .models import Bibliotheque

from .models import Book,BookInstance

# Register your models here.
admin.site.register(Bibliotheque)