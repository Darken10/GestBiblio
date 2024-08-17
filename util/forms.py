
from util.models import Utilisateur,Abonne,Admin,Bibliothecaire,Visiteur
from django.core.exceptions import ValidationError
from django import forms
from livre.models import Bibliotheque

class UtilisateurForm(forms.ModelForm):
    """Form definition for MODELNAME."""

    class Meta:
        """Meta definition for MODELNAMEform."""

        model = Utilisateur
        fields = ['nom','prenom','numero','matricule','password']
        
        
    def clean_numero(self):
        numero = self.cleaned_data.get('numero')
        if not numero.isdigit():
            raise ValidationError("Le numéro doit contenir des chiifres")
        if len(numero)!=8:
            raise ValidationError("Le numero doit contenir 8 Chiffres.")
        return numero
        

class AbonneForm(forms.ModelForm):
    """Form definition for Abonne."""

    class Meta:
        """Meta definition for Abonneform."""

        model = Abonne
        fields = ['nom','prenom','numero','email','filiere',
        #'photo'
        ]
        widgets = {
            'nom':forms.TextInput(attrs={'oninput':'this.value.toUpperCase()','class':'form-control','placeholder':"nom"}),
            'prenom':forms.TextInput(attrs={'oninput':'capitalizeFirstLetter(this)','class':'form-control','placeholder':"prenom"}),
            'numero':forms.TextInput(attrs={'placeholder':'entrez votre numero','class':'form-control','placeholder':"numero"}),
            'filiere':forms.TextInput(attrs={'class':'form-control','placeholder':"filiere"}),
            'email':forms.TextInput(attrs={'class':'form-control','placeholder':"email"})
        }
    def clean_numero(self):
        numero = self.cleaned_data.get('numero')
        if not numero.isdigit():
            raise ValidationError("Le numéro doit contenir des chiifres")
        if len(numero)!=8:
            raise ValidationError("Le numero doit contenir 8 Chiffres.")
        return numero



class VisiteurForm(forms.ModelForm):
    """Form definition for Visiteur."""

    class Meta:
        """Meta definition for Visiteurform."""

        model = Visiteur
        fields = ['nom','prenom','numero','motif','filiere']
        widgets = {
            'nom':forms.TextInput(attrs={'oninput':'this.value.toUpperCase()','class':'form-control','placeholder':"nom"}),
            'prenom':forms.TextInput(attrs={'oninput':'capitalizeFirstLetter(this)','class':'form-control','placeholder':"Prenom"}),
            'filiere':forms.TextInput(attrs={'placeholder':'filiere:ESI par exemple','class':'form-control'}),
            'numero':forms.TextInput(attrs={'placeholder':'entrez votre numero','class':'form-control'}),
            'motif':forms.Textarea(attrs={'placeholder':'entrez le Motif','class':'form-control'}),
            #'date_partie':forms.DateTimeInput(attrs={'type':'time','class':'form-control'})
        }
    def clean_numero(self):
        numero = self.cleaned_data.get('numero')
        """if not numero.isdigit():
            raise ValidationError("Le numéro doit contenir des chiffres")
        if len(numero)!=8:
            raise ValidationError("Le numero doit contenir 8 Chiffres.")"""
        return numero

class BibliothecaireConnecteForm(forms.ModelForm):
    """Form definition for BibliothecaireConnecte."""

    class Meta:
        """Meta definition for BibliothecaireConnecteform."""

        model = Bibliothecaire
        fields = ['numero','password','bibliotheque']
        bibliotheque = Bibliotheque.objects.all()
        widgets = {
            'password':forms.PasswordInput(attrs={'placeholder':'saisir mot de passe','class':'form-control'}),
            'numero':forms.TextInput(attrs={'placeholder':'entrez votre numero','class':'form-control'}),
            'bibliotheque':forms.Select(choices=bibliotheque, attrs={'placeholder':'Choisire votre Bibliotheque','class':'form-control'})
        }

    def clean_numero(self):
        numero = self.cleaned_data.get('numero')
        if not numero.isdigit():
            raise ValidationError("Le numéro doit contenir des chiifres")
        if len(numero)!=8:
            raise ValidationError("Le numero doit contenir 8 Chiffres.")
        return numero

class BibliothecaireForm(UtilisateurForm):
    """Form definition for Bibliothecaire."""

    class Meta:
        """Meta definition for Bibliothecaireform."""

        model = Bibliothecaire
        fields = ['nom','prenom','numero','matricule','password']
        widgets = {
            'nom':forms.TextInput(attrs={'oninput':'this.value.toUpperCase()','class':'form-control','placeholder':"Nom"}),
            'prenom':forms.TextInput(attrs={'oninput':'capitalizeFirstLetter(this)','class':'form-control','placeholder':"Prenom"}),
            'numero':forms.TextInput(attrs={'class':'form-control','placeholder':"Numero"}),
            #'email':forms.TextInput(attrs={'class':'form-control','placeholder':"email"}),
            'matricule':forms.TextInput(attrs={'class':'form-control','placeholder':"Numero Matricule"}),
            'password':forms.PasswordInput(attrs={'placeholder':'Mot de Passe','class':'form-control'}),
        }
    def clean_numero(self):
        numero = self.cleaned_data.get('numero')
        if not numero.isdigit():
            raise ValidationError("Le numéro doit contenir des chiifres")
        if len(numero)!=8:
            raise ValidationError("Le numero doit contenir 8 Chiffres.")
        return numero

class AdminForm(UtilisateurForm):
    """Form definition for Admin."""

    class Meta:
        """Meta definition for Adminform."""

        model = Admin
        fields = ['nom','prenom','numero','matricule','password']
        widgets = {
            'password':forms.PasswordInput(attrs={'paaceholder':'saisir mot de passe'}),
            'numero':forms.TextInput(attrs={'placeholder':'entrez votre numero'})
        }
    def clean_numero(self):
        numero = self.cleaned_data.get('numero')
        if not numero.isdigit():
            raise ValidationError("Le numéro doit contenir des chiifres")
        if len(numero)!=8:
            raise ValidationError("Le numero doit contenir 8 Chiffres.")
        return numero



class BibliothequeForm(forms.ModelForm):

    class Meta:
        model = Bibliotheque
        fields = ['nom','filiere','site']
        widgets = {
            'nom':forms.TextInput(attrs={'oninput':'this.value.toUpperCase()','class':'form-control','placeholder':"Nom"}),
            'filiere':forms.TextInput(attrs={'oninput':'capitalizeFirstLetter(this)','class':'form-control','placeholder':"filiere"}),
            'site':forms.TextInput(attrs={'class':'form-control','placeholder':"Localisation"}),
        }
        