from django.shortcuts import render,HttpResponse,redirect
from .models import *
from util.models import *
from livre.models import *
from .forms import EmpruntForm
import datetime
from django.contrib import messages

# Create your views here.
def index_emprunt(request):
    bibliotheque = Bibliothecaire.objects.all()[0].bibliotheque
    emprunts = Emprunt.objects.filter(exemplaire__statut='Emprunter',return_at__isnull=True,biblio__bibliotheque=bibliotheque)
    context = {
        'emprunts':emprunts,
    }

    return render(request, 'emprunt/liste-emprunt.html', context)

def create_emprunt(request):
    if request.method == 'POST':
        deja = Emprunt.objects.filter(return_at__isnull=True ,abonne_id=request.POST['abonne'])
        if len(deja)<2 or (len(deja)<3 and Abonne.objects.get(pk=request.POST['abonne']).is_professeur):
            form = EmpruntForm(request.POST)  
            emprunt = form.save(commit=False)  
            #emprunt.remise_date =  datetime.datetime.now().__radd__()         
            emprunt.biblio = Bibliothecaire.objects.all()[0]     
            exemplaire = BookInstance.objects.get(pk=request.POST['exemplaire'])
            if exemplaire.statut == 'Disponible' :
                exemplaire.statut = 'Emprunter'
                emprunt.save()
                exemplaire.save()
                messages.success(request, f"Le livre a bien ete emprunter a {emprunt.abonne.nom} {emprunt.abonne.prenom}")
            else : 
                messages.error(request, f"Cet exemplaire a deja ete emprunter ")
        else :
            messages.error(request, f"Ce Anbonne ne peut plus prendre de livre car il a atteint le nombre max")

        return redirect('emprunt-index')
    else :
        form = EmpruntForm(request.POST)
    context = {
        'form':form
    }
    return render(request, 'emprunt/create-form-emprunt.html', context)


def remise_emprunt(request):
    print(f"+++++++++++++{datetime.datetime.today()}")
    if request.method == 'POST':
        emprunt = Emprunt.objects.get(pk=request.POST['emprunt'])
        exemplaire = emprunt.exemplaire
        
        if exemplaire.statut == 'Emprunter' and emprunt.return_at is None:
            exemplaire.statut = 'Disponible'
            emprunt.return_at = datetime.datetime.today()
            exemplaire.save()
            emprunt.save()

            messages.success(request, f"Remise du livre {exemplaire.code} - {exemplaire.book.title} a bien ete enregistrer")
        else : 
            messages.error(request, f"Le Livre a deja ete remise")
    else : 
        messages.error(request, f"Une erreur es survenu lors de l'enregistrement")

    return redirect('emprunt-index')
        


