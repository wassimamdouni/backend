# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from datetime import datetime, timedelta
import os

from phonenumber_field.modelfields import PhoneNumberField
import phonenumbers

def filepath(request, filename):
    old_filename = filename
    timeNow = datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('Voitures/', filename)


def filepathClient_Photo(request, filename):
    old_filename = filename
    timeNow = datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('Clients/Photo/', filename)

def filepathClient_Cin_Passport(request, filename):
    old_filename = filename
    timeNow = datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('Clients/Cin_Passport/', filename)
def filepathClient_Parmis(request, filename):
    old_filename = filename
    timeNow = datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('Clients/Parmis/', filename)


def filepathAdmins(request, filename):
    old_filename = filename
    timeNow = datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('Admins/', filename)

def filepathPost(request, filename):
    old_filename = filename
    timeNow = datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('Post/', filename)

def filepathMarquer(request, filename):
    old_filename = filename
    timeNow = datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('Marquer/', filename)

def filepathGallery(request, filename):
    old_filename = filename
    timeNow = datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('Gallery/', filename)


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()



class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()



#*********************************************************************************************
class Admin(models.Model):
    class StatutAdmin(models.TextChoices):
        ACTIVATED = 'Activated', ('Activated')
        DEACTIVATED = 'Deactivated', ('Deactivated') 

    id=models.AutoField(primary_key=True,auto_created=True,unique=True,blank=True,null=False,verbose_name="Admin")
    nom_prenom = models.CharField(max_length=100,null=False, blank=True)
    telephone = PhoneNumberField(unique=True,null=False, blank=True)
    email = models.CharField(max_length=100,unique=True,null=False,blank=True)
    mot_de_passe = models.CharField(max_length=8, null=False, blank=True)
    photo = models.ImageField(upload_to=filepathAdmins , null=False ,blank=True,default="default_profile_picture.png")
    statutAdmin= models.CharField(max_length=11,blank=True,choices=StatutAdmin.choices,default=StatutAdmin.DEACTIVATED)
    token = models.TextField( blank=True, null=False,default="")
    def __str__(self):
        return '({}) {}'.format(self.id,self.nom_prenom)
    
    
class Post(models.Model):
    id=models.AutoField(primary_key=True,auto_created=True,unique=True,blank=True,null=False,verbose_name="Post")
    title = models.CharField(max_length=100,blank=True,null=False)
    descriptions = models.TextField(max_length=255,blank=True,null=False)
    date_depart = models.DateTimeField( blank=True,null=False ,default=datetime.now)
    date_fin = models.DateTimeField( blank=True,null=False ,default=(datetime.now() + timedelta(days=3)))
    lien = models.URLField(max_length=255 , null=False , default="https://www.tiktok.com/@neapolis.car")
    photo = models.ImageField(upload_to=filepathPost,blank=False, null=False ,default="default_image.jpg")
    
    def __str__(self):
        return '({}) {}'.format(self.id,self.title)

#----------------------------------------------------       
class Client(models.Model):
    class StatutClient(models.TextChoices):
        ACTIVATED = 'Activated', ('Activated')
        DEACTIVATED = 'Deactivated', ('Deactivated') 

    id=models.AutoField(primary_key=True,auto_created=True,unique=True,blank=True,null=False,verbose_name="Client")
    nomprenom = models.CharField(max_length=50, blank=True,null=False)
    
    cin_passport = models.CharField(max_length=12,blank=True, null=False)
    numeroparmis = models.CharField(max_length=50, blank=True, null=False)
    
    telephone = PhoneNumberField(null=False, blank=True,unique=False)
    email = models.EmailField(max_length=254,unique=True,blank=True, null=False)
    mot_de_passe = models.CharField(max_length=255,blank=True, null=False)

    paye = models.CharField(max_length=100, blank=True, null=False)
    ville = models.CharField(max_length=50, blank=True, null=False)
    region = models.CharField(max_length=100, blank=True, null=False)
    numerorue = models.CharField(max_length=50, blank=True, null=False)
    nomentrprise = models.CharField(max_length=50, blank=True, null=False)
    
    photo = models.ImageField(upload_to=filepathClient_Photo , null=False , blank=True,default="default_profile_picture.png")
    photo_cin_passport = models.ImageField(upload_to=filepathClient_Cin_Passport , null=False , blank=True,default="default_image.jpg")
    photo_parmis = models.ImageField(upload_to=filepathClient_Parmis, null=False , blank=True,default="default_image.jpg")
    
    points = models.IntegerField(default=0, blank=True, null=False)

    statutClient= models.CharField(max_length=11,blank=True,choices=StatutClient.choices,default=StatutClient.DEACTIVATED)
    
    token = models.TextField( blank=True, null=False,default="")

    def __str__(self):
        return '({}) {}'.format(self.id,self.nomprenom)

#----------------------------------------------------    
class Marquer(models.Model):
    id=models.AutoField(primary_key=True,auto_created=True,unique=True,blank=True,null=False,verbose_name="Marquer")
    nom = models.CharField(max_length=50, blank=True, null=True)
    logo =models.ImageField(upload_to=filepathMarquer , null=True ,blank=True,default="default_profile_picture.png")
    def __str__(self):
        return '({}) {}'.format(self.id,self.nom)
    
class Voiture(models.Model):

    numero_series = models.CharField(primary_key=True,unique=True, blank=True, null=False,verbose_name="Voiture",max_length=20)
    modele = models.CharField(max_length=50, blank=True, null=False)
    class_voiture = models.CharField(max_length=10, blank=True, null=False)
    annee = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=False)

    boite = models.CharField(max_length=10,    blank=True, null=False)
    nb_seats = models.IntegerField( default=0, blank=True, null=False )
    nb_bags = models.IntegerField(  default=0, blank=True, null=False )
    nb_ports = models.IntegerField( default=0, blank=True, null=False )

    color = models.CharField(max_length=20, blank=True, null=False)

    etat = models.CharField(max_length=10, blank=True, null=False)
    description = models.CharField(max_length=255, blank=True, null=True)
    
    caution= models.FloatField(default=0,blank=True, null=False)
    prix_jour = models.FloatField(default=0,blank=True, null=False )
    
    photo = models.ImageField(upload_to=filepath , null=False ,blank=True, default="default_image.jpg")    
    id_marquer = models.ForeignKey(Marquer , models.CASCADE , db_column='id',blank=True,null=False)

    def GroupByModele():
        voitures = Voiture.objects.all()
        voiture = []
        model=""
        for item in voitures:
            if model != item.modele :
                model= item.modele
                voiture.append(item)
        return voiture
    
    def __str__(self):
        return '({}) {} {} {} : {}'.format(self.numero_series,self.modele,self.class_voiture,self.annee,self.id_marquer)

class Options(models.Model):
    id=models.AutoField(primary_key=True,auto_created=True,unique=True,blank=True,null=False,verbose_name="Options")
    title = models.CharField(max_length=255, blank=True, null=False)
    descriptions = models.TextField(max_length=255,blank=True,null=False)
    numero_series = models.ForeignKey(Voiture, models.CASCADE, db_column='numero_series', blank=True, null=False)

    def __str__(self):
        return '({}) {} : ({})'.format(self.id,self.title,self.numero_series)
   
#----------------------------------------------------  

class Demande(models.Model):
    class TypeDemande(models.TextChoices):
        RESERVATION = 'Reservation', ('Reservation')
        EXURCION = 'Exurcion', ('Exurcion') 
        TRANSFER = 'Transfer', ('Transfer') 

    class EtatDemande(models.TextChoices):
        ATTENTE = 'Attente', ('Attente')
        ENCOURS = 'EnCours', ('En Cours')
        TERMINER = 'Terminer', ('Terminer')
        Annulater = 'Annuler', ('Annuler')

    
    id=models.AutoField(primary_key=True,auto_created=True,unique=True,blank=True,null=False,verbose_name="Demande")
    type = models.CharField(max_length=11,blank=True,choices=TypeDemande.choices,default=TypeDemande.RESERVATION)
    date = models.DateTimeField(default=datetime.now, blank=True, null=False)
    etat = models.CharField(max_length=11,blank=True,choices=EtatDemande.choices,default=EtatDemande.ATTENTE)
    id_client = models.ForeignKey(Client, models.DO_NOTHING, db_column='id_client', blank=True, null=True)
    
    def __str__(self):
        return '({}) [{}] [{}] : ({}) ({} TND)'.format(self.id,self.type,self.etat,self.id_client,self.date)
    
#---------------------------------------------------- 

class Service(models.Model):
    id=models.AutoField(primary_key=True,auto_created=True,unique=True,blank=True,null=False,verbose_name="Service")
    nom = models.CharField(max_length=255, blank=True, null=False)
    descreptions = models.CharField(max_length=255, blank=True, null=True)
    id_demande = models.ForeignKey('Demande', models.CASCADE, db_column='id_demande', blank=True, null=False)
    prix = models.FloatField(default=0,blank=True, null=False)

    def __str__(self):
        return '({}) {} : ({}) ({} TND)'.format(self.id,self.nom,self.id_demande,self.prix)
    
#---------------------------------------------------- 

class Reservation(models.Model):
    id=models.AutoField(primary_key=True,auto_created=True,unique=True,blank=True,null=False,verbose_name="Reservation")
    bureau_predre_la_voiture = models.CharField(max_length=100, blank=True, null=False)
    bureau_deposer_la_voiture = models.CharField(max_length=100, blank=True, null=False)
    date_depar = models.DateTimeField(default=datetime.now, blank=True, null=False)
    date_arriver = models.DateTimeField(default=(datetime.now() + timedelta(days=6)), blank=True, null=False)
    numero_series = models.ForeignKey('Voiture', models.DO_NOTHING, db_column='numero_series', blank=True, null=False)
    id_demande = models.ForeignKey(Demande, models.CASCADE, db_column='id_demande', blank=True, null=False)

    def __str__(self):
        return '({}) [{}] [{}] : {}--{} | {}--{}'.format(self.id,self.id_demande,self.numero_series,self.bureau_predre_la_voiture,self.bureau_deposer_la_voiture,self.date_depar,self.date_arriver)

#----------------------------------------------------  

class ListExurcion(models.Model):
    class Location(models.TextChoices):
        DE_HAMMAME_A_TUNIS_CARTHAGE = 'De Hammamet a Tunis Carthage', ('De Hammamet a Tunis Carthage')
        DE_HAMMAME_A_kAIROUAN = 'De Hammamet a Kairoun', ('De Hammamet a Kairoun')
        DE_HAMMAME_A_SOUSSE = 'De Hammamet a Sousse', ('De Hammamet a Sousse')
        DE_HAMMAME_A_HAMMAME_YASMINE = 'De Hammamet a Hammamet Yasmine', ('De Hammamet a Hammamet Yasmine') 
        
    id=models.AutoField(primary_key=True,auto_created=True,unique=True,blank=True,null=False,verbose_name="ListExurcion")
    address_depart= models.CharField(max_length=50,choices=Location.choices,blank=True, null=False)
    description = models.CharField(max_length=255, blank=True, null=True)
    prix = models.FloatField(default=0,blank=True, null=False)

    def __str__(self):
        return '({}) {} ({} TND)'.format(self.id,self.address_depart,self.prix)

class Gallery(models.Model):    
    idPhoto=models.AutoField(primary_key=True,auto_created=True,unique=True,verbose_name="Identifiant Gallery")
    photo= models.ImageField(upload_to=filepathGallery , null=False ,blank=True, default="default_image.jpg")
    titleGallery=models.CharField(max_length=2048,unique=True,null=False ,blank=True)
    listExurcion=models.ForeignKey('ListExurcion',on_delete=models.CASCADE)

    def __str__(self):
        return '({}) {}'.format(self.idPhoto,self.titleGallery)

class Exurcion(models.Model):
    id=models.AutoField(primary_key=True,auto_created=True,unique=True,blank=True,null=False,verbose_name="Exurcion")
    date_depar = models.DateTimeField(default=(datetime.now() + timedelta(days=2)),blank=True, null=False)
    id_ListExurcion = models.ForeignKey('ListExurcion', models.CASCADE, db_column='id_ListExurcion',blank=True, null=False)
    numero_series = models.ForeignKey('Voiture', models.CASCADE, db_column='numero_series',blank=True, null=False)
    id_demande = models.ForeignKey('Demande', models.CASCADE, db_column='id_demande',blank=True, null=False)

    def __str__(self):
        return '({}) [{}] [{}] : {} | {}'.format(self.id,self.id_demande,self.numero_series,self.id_ListExurcion,self.date_depar)

#----------------------------------------------------  

class ListTransfer(models.Model):
    class Location(models.TextChoices):
        
        HAMMAMET = 'Hammamet', ('Hammamet')
        TUNISIE = 'Tunisie', ('Tunisie')
        ENFIDHA = 'Enfidha', ('Enfidha')
        MONASTIR = 'Monastir', ('Monastir')
        SFAX = 'Sfax', ('Sfax')
        SOUSSE = 'Sousse', ('Sousse') 
        
    id=models.AutoField(primary_key=True,auto_created=True,unique=True,blank=True,null=False,verbose_name="ListTransfer")
    address_depart= models.CharField(max_length=8,choices=Location.choices,blank=True, null=False)
    address_fin= models.CharField(max_length=8,choices=Location.choices,blank=True, null=False)
    prix = models.FloatField(default=0,blank=True, null=False )

    def __str__(self):
        return '({}) {}--{} ({} TND)'.format(self.id,self.address_depart,self.address_fin,self.prix)
    
class Transfer(models.Model):
    id=models.AutoField(primary_key=True,auto_created=True,unique=True,blank=True,null=False,verbose_name="Transfer")
    date_depar = models.DateTimeField( blank=True, null=False,default=(datetime.now() + timedelta(days=2)))
    id_ListTransfer = models.ForeignKey('ListTransfer', models.CASCADE, db_column='id_ListTransfer',blank=True, null=False)
    numero_series = models.ForeignKey('Voiture', models.CASCADE, db_column='numero_series', blank=True, null=False)
    id_demande = models.ForeignKey(Demande, models.CASCADE, db_column='id_demande', blank=True, null=False)
    
    def __str__(self):
        return '({}) [{}] [{}] : {} | {}'.format(self.id,self.id_demande,self.numero_series,self.id_ListTransfer,self.date_depar)

#----------------------------------------------------  

class Paiment(models.Model):
    class TypePaiment(models.TextChoices):
        CASH = 'Cash', 'Cash'
        CARD = 'Card', 'Card'
        CHECK = 'Check', 'Check'

    id = models.AutoField(primary_key=True,auto_created=True,unique=True,blank=True,null=False,verbose_name="Paiment")
    prix = models.FloatField(default=0, blank=True, null=True)
    date = models.DateTimeField( blank=True, null=False,default=datetime.now)
    type= models.CharField(max_length=8,blank=True, null=False,choices=TypePaiment.choices,default=TypePaiment.CARD)
    id_client = models.ForeignKey(Client, models.CASCADE, db_column='id_client', blank=True, null=False)
    id_demande = models.ForeignKey(Demande, models.CASCADE, db_column='id_demande', blank=True, null=False)
    
    def __str__(self):
        return '({}) {} -- {} ({} TND) ({} TND)'.format(self.id,self.id_client,self.id_demande,self.prix,self.type)

class Annulation(models.Model):
    id = models.AutoField(primary_key=True,auto_created=True,unique=True,blank=True,null=False,verbose_name="Annulation")
    date = models.DateTimeField( blank=True, null=False,default=datetime.now)
    description = models.TextField(max_length=255,blank=True,null=False)
    id_demande = models.ForeignKey(Demande , models.CASCADE , db_column='id_demand')

    def __str__(self):
        return '({}) -- ({}) -- {}'.format(self.id,self.id_demande,self.date)