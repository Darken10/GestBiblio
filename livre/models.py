from django.db import models
from util.models import *

# Create your models here.



class Dicipline(models.Model):
    '''Model definition for Dicipline.'''
    code = models.CharField(max_length=12,primary_key=True)
    name = models.CharField(max_length=100)
    
    class Meta:
        '''Meta definition for Dicipline.'''
        verbose_name = 'Dicipline'
        verbose_name_plural = 'Diciplines'

    def __str__(self):
        return f"{self.code} - {self.name}"


class Etager(models.Model):
    '''Model definition for Etager.'''
    numero = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50,blank=True)
    bibliotheque = models.ForeignKey(Bibliotheque,on_delete=models.CASCADE,null=True)
    created_at = models.DateTimeField(auto_now=True)


    class Meta:
        '''Meta definition for Etager.'''

        verbose_name = 'Etager'
        verbose_name_plural = 'Etagers'

    def __str__(self):
        return f"{self.numero} => {self.name}"


class Section(models.Model):
    '''Model definition for Section.'''
    numero = models.IntegerField()
    name = models.CharField(max_length=50,blank=True)
    etager = models.ForeignKey(Etager,models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        '''Meta definition for Section.'''

        verbose_name = 'Section'
        verbose_name_plural = 'Sections'

    def __str__(self):
        return f" {self.name} => {self.etager.name}"


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

   
class MaisonEdition(models.Model):
    nom=models.CharField(max_length=100,null=False,blank=False,default='')
    pays=models.CharField(max_length=50,null=False,blank=False,default='')
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.nom



class Book(models.Model):
    cote = models.CharField(max_length=12,primary_key=True)
    isbn = models.CharField(max_length=20,null=True)
    title = models.CharField(max_length=100)
    desciption = models.TextField(blank=True)
    authors = models.ManyToManyField(Author)
    dicipline = models.ForeignKey(Dicipline,on_delete=models.CASCADE)
    maison_edition = models.ForeignKey(MaisonEdition,on_delete=models.SET_NULL,null=True)
    published_at = models.DateField()
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Livre'
        verbose_name_plural = 'Livres'

    def __str__(self):
        return f"{self.cote} => {self.dicipline.name} => {self.title}"


class BookInstance(models.Model):
    '''Model definition for BookInstance.'''
    STATUT = {
        ('Disponible','Disponible'),
        ('Emprunter','Emprunter'),
        ('Maintenance','Maintenance'),
        ('Endommager','Endommager'),
    }
    code = models.CharField(max_length=12)
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    section = models.ForeignKey(Section,null=True,on_delete=models.SET_NULL)
    statut = models.CharField(max_length=12,choices=STATUT,blank=True,default='Maintenance')
    bibliotheque = models.ForeignKey(Bibliotheque,on_delete=models.CASCADE,null=True)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        '''Meta definition for BookInstance.'''
        verbose_name = 'BookInstance'
        verbose_name_plural = 'BookInstances'

    def __str__(self):
        return f"{self.code} => {self.book.title}"

