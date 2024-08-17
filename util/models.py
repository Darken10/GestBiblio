from django.db import models



class Utilisateur(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    numero = models.CharField(max_length=25,unique=True,null=False)
    matricule = models.CharField(max_length=25,blank=True)
    password = models.CharField(max_length=130)
    is_admin = models.BooleanField(default=False)
    is_biblio = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Utilisateur:{self.nom} {self.prenom}'

class Admin(Utilisateur):
    email = models.EmailField(null=True)
    def __str__(self):
        return f'Admin:{self.nom} {self.prenom}'
    
    @property
    def bibliothecaires(self):
        return self.admin_set




class Bibliotheque(models.Model):
    nom = models.CharField(max_length=100)
    filiere = models.CharField(max_length=100)
    site = models.CharField(max_length=100)
    admin = models.ForeignKey(Admin,on_delete=models.CASCADE,null=True)


    def __str__(self):
        return str(f"{self.nom} - {self.filiere} ")

class Bibliothecaire(Utilisateur):
    Admin = models.ForeignKey(Admin,on_delete=models.CASCADE)
    bibliotheque = models.ForeignKey(Bibliotheque,null=True,on_delete=models.SET_NULL)
    def __str__(self):
        return f'Bibliothecaire:{self.nom} {self.prenom}'

    @property
    def abonnes(self):
        return self.biblio_set
    
    @property
    def visiteurs(self):
        return self.visiteur_set
    




class Abonne(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    numero = models.CharField(max_length=10,unique=True,null=False)
    filiere = models.CharField(max_length=100)
    is_professeur = models.BooleanField(default=False)
    is_etudiant = models.BooleanField(default=False)
    email = models.EmailField(null=False)
    biblio = models.ForeignKey(Bibliothecaire,on_delete=models.CASCADE)
    photo = models.ImageField(null = False)
    bibliotheque = models.ForeignKey(Bibliotheque,on_delete=models.CASCADE)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Abonne:{self.nom} {self.prenom}'


class Visiteur(models.Model):
    nom = models.CharField(max_length=50,null=False)
    prenom = models.CharField(max_length=50,null=False)
    numero = models.BigIntegerField(null=False)
    motif = models.TextField(null=False)
    filiere = models.CharField(max_length=100,null=False)
    biblio = models.ForeignKey(Bibliothecaire,on_delete=models.CASCADE)
    bibliotheque = models.ForeignKey(Bibliotheque, on_delete=models.CASCADE)
    date_heure_arriver = models.DateTimeField(auto_now_add=True)
    date_partie = models.DateTimeField(null=True)

    def __str__(self):
        return f'Visiteur:{self.nom} {self.prenom}'
# Create your models here.

