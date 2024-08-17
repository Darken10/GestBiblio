from django.db.models import Count,Sum
from django.shortcuts import render,HttpResponse,redirect
from .models import *
from util.forms import VisiteurForm
from util.models import Visiteur,Bibliothecaire,Abonne
from .forms import *
from livre.models import *
import datetime
from django.contrib import messages
from emprunt.models import Emprunt

# Create your views here.

def index(request):
    form = VisiteurForm(request.POST)
    bibliothecaire = Bibliothecaire.objects.all()[0]
    bibliotheque = bibliothecaire.bibliotheque
    #visiteur_count = len(Visiteur.objects.filter(date_heure_arriver__gte=datetime.datetime.today().date(),biblio=Bibliothecaire.objects.get(pk=2)))
    books = Book.objects.annotate(nb_exemplaire=Count('bookinstance')).filter(nb_exemplaire__gt=0,bookinstance__bibliotheque=bibliotheque).aggregate(nb = Sum('nb_exemplaire'))
    print(f"++++++++++++++++++++{books['nb']}")
    visiteur_count = len(Visiteur.objects.filter(date_heure_arriver__gte=datetime.datetime.today().date(),bibliotheque=bibliotheque))
    abonne_count = len(Abonne.objects.filter(bibliotheque=bibliotheque))
    nb_livre = books['nb']
    nb_emprunt = len(Emprunt.objects.filter(abonne__bibliotheque=bibliotheque))
    today = datetime.datetime.today()
    stat_emprunts = {
        'jan': len(Emprunt.objects.filter(abonne__bibliotheque=bibliotheque,created_at__lte="2024-02-01",created_at__gte="2024-01-01")),
        'fev': len(Emprunt.objects.filter(abonne__bibliotheque=bibliotheque,created_at__lte='2024-03-01',created_at__gte='2024-02-01')),
        'mar': len(Emprunt.objects.filter(abonne__bibliotheque=bibliotheque,created_at__lte='2024-04-01',created_at__gte='2024-03-01')),
        'avr': len(Emprunt.objects.filter(abonne__bibliotheque=bibliotheque,created_at__lte='2024-05-01',created_at__gte='2024-04-01')),
        'mai': len(Emprunt.objects.filter(abonne__bibliotheque=bibliotheque,created_at__lte='2024-06-01',created_at__gte='2024-05-01')),
        'jun': len(Emprunt.objects.filter(abonne__bibliotheque=bibliotheque,created_at__lte='2024-07-01',created_at__gte='2024-06-01')),
        'jul': len(Emprunt.objects.filter(abonne__bibliotheque=bibliotheque,created_at__lte='2024-08-01',created_at__gte='2024-07-01')),
        'aut': len(Emprunt.objects.filter(abonne__bibliotheque=bibliotheque,created_at__lte='2024-09-01',created_at__gte='2024-08-01')),
        'sep': len(Emprunt.objects.filter(abonne__bibliotheque=bibliotheque,created_at__lte='2024-10-01',created_at__gte='2024-09-01')),
        'oct': len(Emprunt.objects.filter(abonne__bibliotheque=bibliotheque,created_at__lte='2024-11-01',created_at__gte='2024-10-01')),
        'nov': len(Emprunt.objects.filter(abonne__bibliotheque=bibliotheque,created_at__lte='2024-12-01',created_at__gte='2024-11-01')),
        'dec': len(Emprunt.objects.filter(abonne__bibliotheque=bibliotheque,created_at__lte='2025-01-01',created_at__gte='2024-12-01')),
    }
    stat_visiteurs = {
        'jan': len(Visiteur.objects.filter(bibliotheque=bibliotheque,date_heure_arriver__lte="2024-02-01",date_heure_arriver__gte="2024-01-01")),
        'fev': len(Visiteur.objects.filter(bibliotheque=bibliotheque,date_heure_arriver__lte='2024-03-01',date_heure_arriver__gte='2024-02-01')),
        'mar': len(Visiteur.objects.filter(bibliotheque=bibliotheque,date_heure_arriver__lte='2024-04-01',date_heure_arriver__gte='2024-03-01')),
        'avr': len(Visiteur.objects.filter(bibliotheque=bibliotheque,date_heure_arriver__lte='2024-05-01',date_heure_arriver__gte='2024-04-01')),
        'mai': len(Visiteur.objects.filter(bibliotheque=bibliotheque,date_heure_arriver__lte='2024-06-01',date_heure_arriver__gte='2024-05-01')),
        'jun': len(Visiteur.objects.filter(bibliotheque=bibliotheque,date_heure_arriver__lte='2024-07-01',date_heure_arriver__gte='2024-06-01')),
        'jul': len(Visiteur.objects.filter(bibliotheque=bibliotheque,date_heure_arriver__lte='2024-08-01',date_heure_arriver__gte='2024-07-01')),
        'aut': len(Visiteur.objects.filter(bibliotheque=bibliotheque,date_heure_arriver__lte='2024-09-01',date_heure_arriver__gte='2024-08-01')),
        'sep': len(Visiteur.objects.filter(bibliotheque=bibliotheque,date_heure_arriver__lte='2024-10-01',date_heure_arriver__gte='2024-09-01')),
        'oct': len(Visiteur.objects.filter(bibliotheque=bibliotheque,date_heure_arriver__lte='2024-11-01',date_heure_arriver__gte='2024-10-01')),
        'nov': len(Visiteur.objects.filter(bibliotheque=bibliotheque,date_heure_arriver__lte='2024-12-01',date_heure_arriver__gte='2024-11-01')),
        'dec': len(Visiteur.objects.filter(bibliotheque=bibliotheque,date_heure_arriver__lte='2025-01-01',date_heure_arriver__gte='2024-12-01')),
    }
    stat_abonnes = {
        'jan': len(Abonne.objects.filter(bibliotheque=bibliotheque, date_creation__lte="2024-02-01",date_creation__gte="2024-01-01")),
        'fev': len(Abonne.objects.filter(bibliotheque=bibliotheque, date_creation__lte='2024-03-01',date_creation__gte='2024-02-01')),
        'mar': len(Abonne.objects.filter(bibliotheque=bibliotheque, date_creation__lte='2024-04-01',date_creation__gte='2024-03-01')),
        'avr': len(Abonne.objects.filter(bibliotheque=bibliotheque, date_creation__lte='2024-05-01',date_creation__gte='2024-04-01')),
        'mai': len(Abonne.objects.filter(bibliotheque=bibliotheque, date_creation__lte='2024-06-01',date_creation__gte='2024-05-01')),
        'jun': len(Abonne.objects.filter(bibliotheque=bibliotheque, date_creation__lte='2024-07-01',date_creation__gte='2024-06-01')),
        'jul': len(Abonne.objects.filter(bibliotheque=bibliotheque, date_creation__lte='2024-08-01',date_creation__gte='2024-07-01')),
        'aut': len(Abonne.objects.filter(bibliotheque=bibliotheque, date_creation__lte='2024-09-01',date_creation__gte='2024-08-01')),
        'sep': len(Abonne.objects.filter(bibliotheque=bibliotheque, date_creation__lte='2024-10-01',date_creation__gte='2024-09-01')),
        'oct': len(Abonne.objects.filter(bibliotheque=bibliotheque, date_creation__lte='2024-11-01',date_creation__gte='2024-10-01')),
        'nov': len(Abonne.objects.filter(bibliotheque=bibliotheque, date_creation__lte='2024-12-01',date_creation__gte='2024-11-01')),
        'dec': len(Abonne.objects.filter(bibliotheque=bibliotheque, date_creation__lte='2025-01-01',date_creation__gte='2024-12-01')),
    }
    #print(f"----------------------------{BookInstance.objects.annotate(Count('emprunts'))}")
    context = {
        'form':form,
        'visiteur_count':visiteur_count,
        'abonne_count':abonne_count,
        'nb_livre' : nb_livre,
        'nb_emprunt' : nb_emprunt,
        'stat_emprunts':stat_emprunts,
        'stat_visiteurs':stat_visiteurs,
        'stat_abonnes':stat_abonnes,

    }

    return render(request, 'livre/index.html', context)

def show(request,id_livre):
    context = {
        'id':id_livre,
        #'etagers': Etager.all()
    }
    print(Etager.objects.all())
    return render(request, 'livre/show.html', context)




#=========Auteur========================================================
def index_auteur(request):
    form = AuthorForm()
    auteurs = Author.objects.all()
    context = {
        'form':form,
        'auteurs' : auteurs,
    }
    return render(request, 'livre/author/index.html', context)

def create_auteur(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)  
        author = form.save(commit=False)            
        author.save()
        messages.success(request,"L'auteur a bien ete enregistre")
        return redirect('author-index')
    else :
        form = AuthorForm(request.POST)
    return render (request, 'livre/author/create-form.html',{'form':form})

def show_auteur(request,id):
    auteur = Author.objects.get(pk=id)
    context = {
        'auteur':auteur,
    }

    return render (request, 'livre/author/show.html',context)

def delete_auteur(request):
    if request.method == "POST":
        auteur = Author.objects.get(pk=request.POST['auteur'])
        auteur.delete()
        messages.success(request,"L'auteur a bien ete Supprimer")
    return redirect('auteur-index')



#=========Dicipline========================================================
def index_dicipline(request):
    form = DiciplineForm()
    diciplines = Dicipline.objects.all()
    context = {
        'form':form,
        'diciplines' : diciplines,
    }
    return render(request, 'livre/dicipline/index.html', context)

def create_dicipline(request):
    if request.method == 'POST':
        form = DiciplineForm(request.POST)  
        dicipline = form.save(commit=False)            
        dicipline.save()
        messages.success(request,"La Dicipline a bien ete enregistre")
        return redirect('dicipline-index')
    else :
        form = DiciplineForm(request.POST)
    return render (request, 'livre/dicipline/create-form.html',{'form':form})

def show_dicipline(request,id):
    dicipline = Dicipline.objects.get(pk=id)
    context = {
        'dicipline':dicipline,
    }

    return render (request, 'livre/dicipline/show.html',context)

def delete_dicipline(request):
    if request.method == "POST":
        print(request.POST['dicipline'])
        dicipline = Dicipline.objects.get(pk=request.POST['dicipline'])
        dicipline.delete()
        messages.success(request,"La Dicipline a bien ete supprimer")
    return redirect('dicipline-index')


#=========Livre========================================================
def index_book(request):
    form = BookForm()
    bibliotheque = Bibliothecaire.objects.all()[0].bibliotheque
    books = Book.objects.alias(nb_exemplaire=Count('bookinstance')).filter(nb_exemplaire__gt=0,bookinstance__bibliotheque=bibliotheque)

    context = {
        'form':form,
        'books' : books,
    }
    return render(request, 'livre/book/index.html', context)

def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)  
        book = form.save(commit=False)            
        book.save()
        messages.success(request,"Le livre a bien ete enregistre")
        
        return redirect('book-index')
    else :
        form = BookForm(request.POST)
    return render (request, 'livre/book/create-form.html',{'form':form})
def show_book(request):
    pass
def delete_book(request):
    if request.method == "POST":
        print(request.POST['book'])
        book = Book.objects.get(pk=request.POST['book'])
        book.delete()
        messages.success(request,"Le livre a bien ete Supprimer")
    return redirect('book-index')



#=========Maison edition========================================================
def index_maison_edition(request):
    form = MaisonEditionForm()
    maison_editions = MaisonEdition.objects.all()
    context = {
        'form':form,
        'maison_editions' : maison_editions,
    }
    return render(request, 'livre/maison-edition/index.html', context)

def create_maison_edition(request):
    if request.method == 'POST':
        form = MaisonEditionForm(request.POST)  
        maison_edition = form.save(commit=False)            
        maison_edition.save()
        messages.success(request,"La Maison d'edition a bien ete enregistre")
        return redirect('maison-edition-index')
    else :
        form = MaisonEditionForm(request.POST)
    return render (request, 'livre/maison-edition/create-form.html',{'form':form})

def show_maison_edition(request):
    pass

def delete_maison_edition(request):
    if request.method == "POST":
        print(request.POST['maison_edition'])
        maison_edition = MaisonEdition.objects.get(pk=request.POST['maison_edition'])
        maison_edition.delete()
        messages.success(request,"La Maison d'edition a bien ete supprimer")
    return redirect('maison-edition-index')
 



#=========Etager========================================================
def index_etager(request):
    form = EtagerForm()
    bibliotheque = Bibliothecaire.objects.all()[0].bibliotheque
    etagers = Etager.objects.filter(bibliotheque=bibliotheque)
    context = {
        'form':form,
        'etagers' : etagers,
    }
    return render(request, 'livre/etager/index.html', context)

def create_etager(request):
    if request.method == 'POST':
        form = EtagerForm(request.POST)  
        etager = form.save(commit=False)    
        #etager.admin = request.user        
        bibliotheque = Bibliothecaire.objects.all()[0].bibliotheque

        etager.bibliotheque = bibliotheque
        etager.save()
        messages.success(request,"L'Etager a bien ete enregistre")
        return redirect('etager-index')
    else :
        form = EtagerForm(request.POST)
    return render (request, 'livre/etager/create-form.html',{'form':form})

def show_etager(request,id):
    pass

def delete_etager(request):
    if request.method == "POST":
        print(request.POST['etager'])
        etager = Etager.objects.get(pk=request.POST['etager'])
        etager.delete()
        messages.success(request,"L'Etager a bien ete Supprimer")
    return redirect('etager-index')



#=========Section========================================================
def index_section(request):
    form = SectionForm()
    sections = Section.objects.all()
    context = {
        'form':form,
        'sections' : sections,
    }
    return render(request, 'livre/section/index.html', context)

def create_section(request):
    if request.method == 'POST':
        form = SectionForm(request.POST)  
        section = form.save(commit=False)
        section.save()
        messages.success(request,"La section a bien ete enregistre")
        return redirect('section-index')
    else :
        form = SectionForm(request.POST)
    return render (request, 'livre/section/create-form.html',{'form':form})

def show_section(request,id):
    pass

def delete_section(request):
    if request.method == "POST":
        print(request.POST['section'])
        section = Section.objects.get(pk=request.POST['section'])
        section.delete()
        messages.success(request,"La Section a bien ete Supprimer")
    return redirect('section-index')



#=========Exemplaire========================================================
def index_exemplaire(request):
    form = ExemplaireForm()
    #biblio = request.user.log.bibliotheque
    biblio = Bibliothecaire.objects.all()[0].bibliotheque

    exemplaires = BookInstance.objects.filter(bibliotheque=biblio)
    context = {
        'form':form,
        'exemplaires' : exemplaires,
    }
    return render(request, 'livre/exemplaire/index.html', context)

def create_exemplaire(request):
    if request.method == 'POST':
        form = ExemplaireForm(request.POST)  
        exemplaire = form.save(commit=False)    
        #exemplaire.admin = request.user 
        bibliotheque = Bibliothecaire.objects.all()[0].bibliotheque     
        exemplaire.bibliotheque = bibliotheque        
        exemplaire.statut = 'Disponible'       
        exemplaire.save()
        print(exemplaire.code)
        messages.success(request,"L'Exemplaire du livre a bien ete enregistre")
        return redirect('exemplaire-index')
    else :
        form = ExemplaireForm(request.POST)
    return render (request, 'livre/exemplaire/create-form.html',{'form':form})
    
def show_exemplaire(request):
    pass

def delete_exemplaire(request):
    if request.method == "POST":
        exemplaire = BookInstance.objects.get(pk=request.POST['exemplaire'])
        exemplaire.delete()
        messages.success(request,"L'Exemplaire du livre a bien ete Supprime")
    return redirect('exemplaire-index')

def change_statut(request):
    if request.method == 'POST':
        print(request.Post)
        return redirect('exemplaire-index')
    else :
        form = ExemplaireForm(request.POST)
    return render (request, 'livre/exemplaire/create-form.html',{'form':form})


#-----------------------------------------++++++++++++++-+++++++++++++++++++--+++++++++++++

def search(request):
    if request.method == 'POST':
        print(request.POST['query'])
        query = request.POST['query']
        livres = BookInstance.objects.filter(book__title__contains=query)
        l = Book.objects.filter(title__contains=query).annotate(nb_exemplaire=Count('bookinstance'))
        
    return HttpResponse(f"{str(livres)} --- {l[0].nb_exemplaire}")
        