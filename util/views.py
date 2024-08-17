import datetime

from django.contrib.auth import login, logout
from django.shortcuts import render, redirect, HttpResponse

from util.forms import *
from util.models import *
from livre.models import *
from emprunt.models import *

from django.contrib import messages


def registerBiblio(request):
    error = False
    msg = ""
    if request.method == 'POST':
        form = BibliothecaireForm(request.POST)
        numero = request.POST.get('numero')
        
        if Utilisateur.objects.filter(numero=numero).exists():
            error = True
           
            context = {
                'error':error,
                'msg':msg,
                'form':form
            }
            messages.error(request,"Ce Biblithecaire existe deja")
            return render(request, 'util/admin-biblio-register-form.html',context)
        else:
            
            bibliothecaire = form.save(commit=False)
            print("===========================",Admin.objects.get(pk=1))
            
            #bibliothecaire.Admin = request.user.id
            bibliothecaire.Admin = Admin.objects.get(pk=1)
            bibliothecaire.save()
            messages.success(request,"Le Biblithecaire a ete bien creer")

        redirect('connecterBiblio')
    else :
        form = BibliothecaireForm(request.POST)
    return render (request, 'util/admin-biblio-register-form.html',{'form':form})

def connecterBiblio(request):
    error = False
    msg = ""
    
    if request.method == 'POST':
        form = BibliothecaireConnecteForm(request.POST)
        numero = request.POST.get('numero')
        password = request.POST.get('password')
        bibliotheque = request.POST.get('bibliotheque')
        
        try:
            user = Utilisateur.objects.get(numero=numero)
        except Utilisateur.DoesNotExist:
            error = True
            msg = "Le Numero et/ou le mot de passe incorrecte"
            messages.error(request,"Le Numero et/ou le mot de passe incorrecte")
            context = {'error': error, 'msg': msg, 'form': form}
            return render(request, 'util/login.html', context)
        
        if password == user.password:
            login(request, user)
            
            print("==========================",{user.numero},{user.id})
            if user.is_admin:
                return redirect('adminHome')
            else:
                bibliothecaire = Bibliothecaire.objects.get(pk=user.id)
                bibliothecaire.bibliotheque_id = bibliotheque
                bibliothecaire.save()
                print(f"---------------------{bibliothecaire.bibliotheque}")
                return redirect('livre-index')
        else:
            error = True
            msg = "Mot de passe incorrect"
            messages.error(request,"Le Numero et/ou le mot de passe incorrecte")

            context = {'error': error, 'msg': msg, 'form': form}
            return render(request, 'util/login.html', context)
    
    else:
        form = BibliothecaireConnecteForm()
    
    return render(request, 'util/login.html', {'form': form})

def registerAbonne(request):
    if request.method == 'POST':
        form = AbonneForm(request.POST)
        numero = request.POST.get('numero')
        email = request.POST.get('email')

        if len(Abonne.objects.filter(numero=numero))>0:
            resultat = Abonne.objects.filter(numero=numero).first()
            print(resultat)
            return redirect('abonnement-show',resultat.id)

        elif len(Abonne.objects.filter(email=email))>0 :
            resultat = Abonne.objects.filter(email=email).first()
            print(resultat)

            return redirect('abonnement-show',resultat.id)
        else:
            abonne=form.save(commit=False)
            #abonne.biblio = request.user.id
            bibliotheque = Bibliothecaire.objects.all()[0].bibliotheque
            abonne.bibliotheque = bibliotheque
            abonne.biblio = Bibliothecaire.objects.get(pk=2)
            print(f"{abonne.biblio} creer par {Bibliothecaire.objects.get(pk=2)}")
            abonne.save() 
            messages.success(request,"L'abonne a bien ete enrgistre")
        return redirect('abonnement-show',abonne.id)
        #return render(request,'detail.html')
    else:
        form = AbonneForm(request.POST)
    return render(request,'util/abonnement/create-form.html',{'form':form})

def showRegister(request,id):
    if id:
        abonne = Abonne.objects.get(pk=id)
    else:
        abonne = Abonne.objects.all()
    return HttpResponse(abonne)
    #return render(request,'showRegister.html',{'abonne':abonne})

def registerVisiteur(request):
    if request.method == 'POST':
        form = VisiteurForm(request.POST)
        visiteur = form.save(commit=False)
        visiteur.biblio = request.user.id
        visiteur.biblio = Bibliothecaire.objects.get(pk=2)
        visiteur.bibliotheque = Bibliothecaire.objects.get(pk=2).bibliotheque
        visiteur.save()

        visiteur.nom = None
        visiteur.prenom = None
        visiteur.numero = None
        visiteur.filiere = None
        visiteur.motif = None
        messages.success(request,"Le Visiteur a bien ete enrgistre")

        return redirect('livre-index')
    else:
        form = VisiteurForm(request.POST)
        return render(request,'registerVisiteur.html',{'form':form})
        
    return redirect('livre-index')
    #


        
def deconnecte(request):
    logout(request)
    return redirect
# Create your views here.

#-------------------------------------------------------------------------
def adminHome(request):
    biblios = Bibliothecaire.objects.all()
    context = {
        'biblios':biblios
    }
    print(biblios)
    
    return render(request, 'util/adminHome.html', context)

def deleteBiblio(request):
    if request.method == "POST":
        biblio = Bibliothecaire(pk=request.POST['biblio'])
        biblio.delete()
        print(f"{biblio} doit etre suprimer")
        messages.success(request,"Le Bibliothecaire a bien ete Supprimer")
        
    return redirect('adminHome')

def profilBibilo(request):
    context = {
        "biblio" : Bibliothecaire.objects.all()[0]
    }
    return render(request, "util/biblio-profile.html", context)
    

#----------------Abonne------------------------------------------------
def abonnement_index(request):
    bibliotheque = Bibliothecaire.objects.all()[0].bibliotheque
    abonnes = Abonne.objects.filter(bibliotheque=bibliotheque)
    context = {
        'abonnes':abonnes
    }
    
    return render(request, 'util/abonnement/index.html', context)

def abonnement_show(request,id):
    abonne = Abonne.objects.get(pk=id)
    bibliotheque = Bibliothecaire.objects.all()[0].bibliotheque
    emprunts = Emprunt.objects.filter(abonne=abonne,biblio__bibliotheque=bibliotheque)
    context = {
        'abonne':abonne,
        'emprunts' : emprunts
    }
    print(abonne)
    
    return render(request, 'util/abonnement/show.html', context)

def abonnement_update(request,id):

    abonne = Abonne.objects.get(pk=id)
    context = {
        'abonne':abonne
    }

    if request.method == 'POST':
        form = AbonneForm(request.POST)

        abonne.nom = request.POST.get('nom')
        abonne.prenom = request.POST.get('prenom')
        abonne.numero = request.POST.get('numero')
        abonne.email = request.POST.get('email')
        abonne.filiere = request.POST.get('filiere')
        abonne.save()
        
        print(abonne)
        messages.success(request,"L'abonne a bien ete enrgistre")

        return redirect('abonnement-show',abonne.id)
    else:
        form = AbonneForm(initial={
            'nom':abonne.nom,
            'prenom':abonne.prenom,
            'numero':abonne.numero,
            'filiere':abonne.filiere,
            'email':abonne.email
        })

    return render(request,'util/abonnement/create-form.html',{'form':form})


def abonnement_delete(request):
    global context
    if request.method == "POST":
        abonne = Abonne(pk=request.POST['abonne'])
        print(f"{abonne} doit etre suprimer")
        abonne.delete()
        nom = f"{abonne.nom} {abonne.prenom}"
        context = {
            'success':True,
            'message':f"L'abonne {nom} a bien été supprimer "
        }
        messages.success(request,"L'abonne a bien ete Supprimer")

    return redirect('abonnement-index')


#---------visiteurs---------------------------------------------------------------
def visiteur_index(request):
    bibliotheque = Bibliothecaire.objects.all()[0].bibliotheque
    visiteurs = Visiteur.objects.filter(bibliotheque=bibliotheque)
    
    if request.method == 'POST':
        form = VisiteurForm(request.POST)
        visiteur = form.save(commit=False)
        #visiteur.biblio = request.user
        visiteur.biblio = Bibliothecaire.objects.get(pk=2)
        
        visiteur.save()

        visiteur.nom = None
        visiteur.prenom = None
        visiteur.numero = None
        visiteur.filiere = None
        visiteur.motif = None
        messages.success(request,"Le Visiteur a bien ete enrgistre")

    else:
        form = VisiteurForm(request.POST)
        
    context = {
        'visiteurs':visiteurs,
        'form':form
    }
    
    return render(request, 'util/visiteur/index.html', context)



def visiteur_delete(request,id):
    if request.method == "POST":
        visiteur = Visiteur(pk=request.POST['visiteur'])
        print(f"{visiteur} doit etre suprimer")
        visiteur.delete()
        messages.success(request,"Le supprimer a bien ete enrgistre")

    return redirect('visiteur-index')

def visiteur_partie(request,id):
    visiteur = Visiteur(pk=id)
    print(f"{visiteur} doit etre partie")
    visiteur.date_partie = datetime.datetime.now()
    visiteur.save()
    messages.success(request,"La sortie du visiteur a bien ete enrgistre")

    return redirect('visiteur-index')


#======== Admin => Bibliotheque========================================================
def index_bibliotheque(request):
    form = BibliothequeForm()
    bibliotheques = Bibliotheque.objects.all()
    context = {
        'form':form,
        'bibliotheques' : bibliotheques,
    }

    print(Bibliotheque.objects.all())
    print("---------------------------------------")
    return render(request, 'livre/bibliotheque/index.html', context)

def create_bibliotheque(request):
    if request.method == 'POST':
        form = BibliothequeForm(request.POST)        
        bibliotheque = form.save(commit=False)        
        #bibliotheque.admin = request.user.id
        bibliotheque.admin = Admin.objects.get(pk=1)
        bibliotheque.save()
        messages.success(request,"Le Bibliotheque a bien ete enrgistre")

        return redirect('bibliotheque-index')
    else :
        form = BibliothequeForm(request.POST)
    return render (request, 'livre/bibliotheque/create-form.html',{'form':form})

def show_bibliotheque(request,id):
    bibliotheque = Bibliotheque.objects.get(pk=id)
    context = {
        'bibliotheque':bibliotheque,
    }

    return render (request, 'livre/bibliotheque/show.html',context)

def delete_bibliotheque(request):
    if request.method == "POST":
        bibliotheque = Bibliotheque.objects.get(pk=request.POST['bibliotheque'])
        bibliotheque.delete()
        messages.success(request,"Le Bibliotheque a bien ete supprimer")

    return redirect('bibliotheque-index')

