from .models import *
from django.core.exceptions import ValidationError
from django import forms


class AuthorForm(forms.ModelForm):

    class Meta:
        model = Author
        fields = ['first_name','last_name']
        widgets = {
            'first_name':forms.TextInput(attrs={'oninput':'this.value.toUpperCase()','class':'form-control','placeholder':"Nom"}),
            'last_name':forms.TextInput(attrs={'oninput':'capitalizeFirstLetter(this)','class':'form-control','placeholder':"filiere"}),
        }
        
    


class DiciplineForm(forms.ModelForm):

    class Meta:
        model = Dicipline
        fields = ['name','code']
        widgets = {
            'name':forms.TextInput(attrs={'oninput':'this.value.toUpperCase()','class':'form-control','placeholder':"Nom"}),
            'code':forms.TextInput(attrs={'oninput':'capitalizeFirstLetter(this)','class':'form-control','placeholder':"Code"}),
        }
        


class MaisonEditionForm(forms.ModelForm):

    class Meta:
        model = MaisonEdition
        fields = ['nom','pays']
        widgets = {
            'nom':forms.TextInput(attrs={'oninput':'this.value.toUpperCase()','class':'form-control','placeholder':"Nom"}),
            'pays':forms.TextInput(attrs={'oninput':'capitalizeFirstLetter(this)','class':'form-control','placeholder':"pays"}),
        }
        


class EtagerForm(forms.ModelForm):

    class Meta:
        model = Etager
        fields = ['numero','name',
        #'bibliotheque'
        ]
        biblioheques = Bibliotheque.objects.all()
        widgets = {
            'numero':forms.TextInput(attrs={'oninput':'this.value.toUpperCase()','class':'form-control','placeholder':"Numero"}),
            'name':forms.TextInput(attrs={'oninput':'capitalizeFirstLetter(this)','class':'form-control','placeholder':"Nom"}),
            #'bibliotheque':forms.Select(choices=biblioheques,attrs={'class':'form-control','placeholder':"bibliotheque"}),
        }
        

class SectionForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = ['numero','name','etager',]
        etagers = Etager.objects.all()
        widgets = {
            'numero':forms.TextInput(attrs={'oninput':'this.value.toUpperCase()','class':'form-control','placeholder':"Numero"}),
            'name':forms.TextInput(attrs={'oninput':'capitalizeFirstLetter(this)','class':'form-control','placeholder':"Nom"}),
            'etager':forms.Select(choices=etagers,attrs={'class':'form-control','placeholder':"Etager"}),
        }
        


class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = [
            'cote',
            'isbn',
            'title',
            'desciption',
            'authors',
            'dicipline',
            'maison_edition',
            'published_at',
        ]

        auteurs = Author.objects.all()
        diciplines = Dicipline.objects.all()
        maison_edition = MaisonEdition.objects.all()
        widgets = {
            'cote':forms.TextInput(attrs={'oninput':'this.value.toUpperCase()','class':'form-control','placeholder':"cote"}),
            'isbn':forms.TextInput(attrs={'oninput':'this.value.toUpperCase()','class':'form-control','placeholder':"ISBN"}),
            'title':forms.TextInput(attrs={'oninput':'capitalizeFirstLetter(this)','class':'form-control','placeholder':"titre"}),
            'desciption':forms.Textarea(attrs={'oninput':'capitalizeFirstLetter(this)','class':'form-control','placeholder':"Description"}),
            'authors':forms.SelectMultiple(choices=auteurs,attrs={'class':'form-control','placeholder':"Auteur"}),
            'dicipline':forms.Select(choices=diciplines,attrs={'class':'form-control ','placeholder':"Dicipline"}),
            'maison_edition':forms.Select(choices=maison_edition,attrs={'class':'form-control ','placeholder':"Maison d'edition"}),
            'published_at':forms.TextInput(attrs={'class':'form-control ','placeholder':"Code",'type':'date'}),
        }
        
    


class ExemplaireForm(forms.ModelForm):

    class Meta:
        model = BookInstance
        fields = ['code','book','statut',
        'section'
        ]
        section = Section.objects.all()
        books = BookInstance.objects.all()
        widgets = {
            'code':forms.TextInput(attrs={'oninput':'this.value.toUpperCase()','class':'form-control','placeholder':"code"}),
            'book':forms.Select(choices=books,attrs={'class':'form-control','placeholder':"Nom"}),
            'section':forms.Select(choices=section,attrs={'class':'form-control','placeholder':"section"}),
        }


class ExemplaireStatutForm(forms.Form):
    model = BookInstance
    fields = ['code','book','statut',
    'section'
    ]
    STATUT = [
        ('Disponible','Disponible'),
        ('Emprunter','Emprunter'),
        ('Maintenance','Maintenance'),
        ('Endommager','Endommager'),
    ]
    section = Section.objects.all()
    books = BookInstance.objects.all()
    widgets = {
        'code':forms.TextInput(attrs={'oninput':'this.value.toUpperCase()','class':'form-control','placeholder':"code"}),
        'book':forms.Select(choices=books,attrs={'class':'form-control','placeholder':"Nom"}),
        'section':forms.Select(choices=section,attrs={'class':'form-control','placeholder':"section"}),
        'statut':forms.Select(choices=STATUT,attrs={'class':'form-control','placeholder':"Statut"}),
    }
