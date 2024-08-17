from django.db import models
from livre.models import BookInstance
from util.models import Abonne,Bibliothecaire

# Create your models here.

class Emprunt(models.Model):
    '''Model definition for Emprunt.'''
    exemplaire = models.ForeignKey(BookInstance, on_delete=models.CASCADE)
    abonne = models.ForeignKey(Abonne, on_delete=models.CASCADE)
    nb_jours = models.IntegerField(default=7)
    biblio = models.ForeignKey(Bibliothecaire,on_delete=models.CASCADE,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    remise_date = models.DateField(auto_now=False, auto_now_add=False,null=True)
    return_at = models.DateTimeField(auto_now=False, auto_now_add=False,null=True)
    
    class Meta:
        '''Meta definition for Emprunt.'''
        verbose_name = 'Emprunt'
        verbose_name_plural = 'Emprunts'

    def __str__(self):
        return f"{self.exemplaire.book.title} - {self.abonne.nom} {self.abonne.prenom}"
