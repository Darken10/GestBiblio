from util.models import Utilisateur,Abonne,Admin,Bibliothecaire,Visiteur
from django.core.exceptions import ValidationError
from django import forms
from livre.models import Bibliotheque,BookInstance
from util.models import Abonne
from emprunt.models import Emprunt

class EmpruntForm(forms.ModelForm):

    class Meta:
        model = Emprunt
        fields = ['exemplaire','abonne','remise_date']
        Ex = BookInstance.objects.filter(statut='Disponible')
        Ab = Abonne.objects.all()
        widgets = {
            'exemplaire':forms.Select(choices=Ex,attrs={'class':'form-control','placeholder':"Exemplaire"}),
            'abonne':forms.Select(choices=Ab, attrs={'class':'form-control','placeholder':"Abonne"}),
            'remise_date':forms.DateInput(attrs={'type':'Date', 'class':'form-control','placeholder':"Date de remise"}),
        }
        