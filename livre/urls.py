from django.urls import path
from .views import *

urlpatterns = [
    path('', index,name="livre-index" ),
    path('auteur/',index_auteur ,name="author-index" ),
    path('show/<int:id_livre>/', show, name="livre-show" ),

    #gestion Globale
    path('search/livre', search, name="livre-search" ),


    
    # gestion auteur
    path('auteur/',index_auteur ,name="auteur-index" ),
    path('auteur/create/',create_auteur ,name="auteur-create" ),
    path('auteur/<int:id>/show/',show_auteur ,name="auteur-show" ),
    path('auteur/delete/',delete_auteur ,name="auteur-delete" ),

    # gestion maison d'edition
    path('maison-edition/',index_maison_edition ,name="maison-edition-index" ),
    path('maison-edition/create/',create_maison_edition ,name="maison-edition-create" ),
    path('maison-edition/<int:id>/show/',show_maison_edition ,name="maison-edition-show" ),
    path('maison-edition/delete/',delete_maison_edition ,name="maison-edition-delete" ),

    # gestion Dicipline
    path('dicipline/',index_dicipline ,name="dicipline-index" ),
    path('dicipline/create/',create_dicipline ,name="dicipline-create" ),
    path('dicipline/<str:id>/show/',show_dicipline ,name="dicipline-show" ),
    path('dicipline/delete/',delete_dicipline ,name="dicipline-delete" ),

    # gestion Section
    path('section/',index_section ,name="section-index" ),
    path('section/create/',create_section ,name="section-create" ),
    path('section/<str:id>/show/',show_section ,name="section-show" ),
    path('section/delete/',delete_section ,name="section-delete" ),

    # gestion Section
    path('exemplaire/',index_exemplaire ,name="exemplaire-index" ),
    path('exemplaire/create/',create_exemplaire ,name="exemplaire-create" ),
    path('exemplaire/<str:id>/show/',show_exemplaire ,name="exemplaire-show" ),
    path('exemplaire/delete/',delete_exemplaire ,name="exemplaire-delete" ),

    # gestion livre
    path('book/',index_book ,name="book-index" ),
    path('book/create/',create_book ,name="book-create" ),
    path('book/<str:id>/show/',show_book ,name="book-show" ),
    path('book/delete/',delete_book ,name="book-delete" ),



    # gestion etager
    path('etager/',index_etager ,name="etager-index" ),
    path('etager/create/',create_etager ,name="etager-create" ),
    path('etager/<int:id>/show/',show_etager ,name="etager-show" ),
    path('etager/delete/',delete_etager ,name="etager-delete" ),



]
