from django.urls import path
from util import views

urlpatterns = [
    path('admin/home/',views.adminHome,name="adminHome"),
    path('admin/home/delete',views.deleteBiblio,name="deleteBiblio"),
    path('registerBiblio/',views.registerBiblio,name="registerBiblio"),
    path('connecterBiblio/',views.connecterBiblio,name="connecterBiblio"),
    path('registerAbonne/',views.registerAbonne,name="registerAbonne"),
    path('showRegister/<int:id>/',views.showRegister,name="showRegister"),

    path('biblio/profile/',views.profilBibilo,name="profilBibilo"),
    path('registerVisiteur/',views.registerVisiteur,name="registerVisiteur"),
    path('abonnements/',views.abonnement_index,name="abonnement-index"),
    path('abonnements/<int:id>',views.abonnement_show,name="abonnement-show"),
    path('abonnements/delete',views.abonnement_delete,name="abonnement-delete"),
    path('abonnements/<int:id>/update',views.abonnement_update,name="abonnement-update"),
    path('visiteurs/',views.visiteur_index,name="visiteur-index"),
    path('visiteurs/<int:id>/delete',views.visiteur_delete,name="visiteur-delete"),
    path('visiteurs/<int:id>/partie',views.visiteur_partie,name="visiteur-partie"),

    #-----------------------------------------------------------------
    #admin gestion bibnlio
    path('biblio/admin',views.index_bibliotheque ,name="bibliotheque-index" ),
    path('biblio/<int:id>/show/admin',views.show_bibliotheque ,name="bibliotheque-show" ),
    path('biblio/create/admin',views.create_bibliotheque ,name="bibliotheque-create" ),
    path('biblio/delete/admin',views.delete_bibliotheque ,name="bibliotheque-delete" ),


]
