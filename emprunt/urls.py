from django.urls import path
from .views import *

urlpatterns = [
    path('', index_emprunt,name="emprunt-index" ),
    path('create/', create_emprunt,name="emprunt-create" ),
    path('remise/', remise_emprunt,name="emprunt-remise" ),
]