import statistics
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponse
from django.shortcuts import render
from datetime import date
from datetime import datetime
from django.utils import timezone
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from polls.models import Admin,  Client , Demande, Gallery, ListExurcion, ListTransfer , Voiture , Transfer , Reservation , Exurcion , Marquer , Options ,  Paiment , Service, Annulation , Post 
from polls.Serializer import AdminsSerializer ,ClientSerializer , DemandeSerializer, ListExurcionSerializer, ListTransferSerializer , ServiceSerializer, TransferSerializer ,ReservationSerializer , MarquerSerializer ,PaimentSerializer ,ServiceSerializer , OptionsSerializer, VoitureSerializer,VoituresSerializer , PostSerializer , GallerySerializer
from django.db import connections
from django.http import JsonResponse
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from datetime import timedelta
from rest_framework import serializers
import json
import logging
import threading
from django.db.models import Subquery, OuterRef
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.hashers import make_password, check_password
import requests
import random
import string
from django.utils.crypto import get_random_string
from django.db import connection

from django.core.serializers import serialize
import requests
import json

from django.conf import settings
from django.core.mail import send_mail
from django.core import serializers
from django.db.models import Q

import firebase_admin
from firebase_admin import credentials,messaging,storage

import firebase_admin
from firebase_admin import credentials
from firebase_admin import messaging

cred = credentials.Certificate('neapoliscaradmin-serviceAccountKey.json')
firebase_admin.initialize_app(cred)

def index(self , request):
    return HttpResponse("Hello, world. You're at the polls index.")

def generate_crypte_id(length=8):
    characters = string.ascii_letters + string.digits
    crypte_id = get_random_string(length, characters)
    return crypte_id

class InserClient(APIView):
    def post(self, request):
        try:
            nomprenom = request.POST['nomprenom']
            numeroparmis = request.POST['numeroparmis']
            nomentrprise = request.POST['nomentrprise']
            cin = request.POST['cin']
            paye = request.POST['paye']
            numerorue = request.POST['numerorue']
            telephone = request.POST['telephone']
            ville = request.POST['ville']
            region = request.POST['region']
            email = request.POST['email']
            mot_de_passe = generate_crypte_id()
            photo_parmis = request.FILES['photo_parmis']
            photo_cin_passport= request.FILES['photo_cin_passport']
            token = request.POST['token']
            photo = request.FILES.get('photo', None)
            nb = Client.objects.filter(email=email).count()
            if(nb==1):
                return  Response({'Reponse':'email déjà utilisé'})
            else:
                mot_de_passe2=make_password(mot_de_passe)
                if(photo==None):
                    client = Client(
                        nomprenom=nomprenom,
                        numeroparmis=numeroparmis,
                        nomentrprise=nomentrprise,
                        cin_passport=cin,
                        paye=paye,
                        numerorue=numerorue,
                        telephone=telephone,
                        ville=ville,
                        region=region,
                        email=email,
                        mot_de_passe=mot_de_passe2,
                        photo_parmis=photo_parmis,
                        photo_cin_passport=photo_cin_passport,
                        statutClient="Activated",
                        token=token,
                        points=0
                        )
                else:
                    client = Client(
                            nomprenom=nomprenom,
                            numeroparmis=numeroparmis,
                            nomentrprise=nomentrprise,
                            cin_passport=cin,
                            paye=paye,
                            numerorue=numerorue,
                            telephone=telephone,
                            ville=ville,
                            region=region,
                            email=email,
                            mot_de_passe=mot_de_passe2,
                            photo_parmis=photo_parmis,
                            photo_cin_passport=photo_cin_passport,
                            photo=photo,
                            statutClient="Activated",
                            token=token,
                            points=0
                            )
                client.save()
                if (client):
                    sujet1 = "Bienvenue a Neapolis car"
                    sujet = sujet1 + " from {}".format(nomprenom)
                    email1 = 'wassim.amdouni28@gmail.com'
                    message1 = " Cher "+nomprenom+", \n Bienvenue à la Société de réservation de voitures ! Nous sommes ravis de vous compter parmi nos membres. \n Votre adresse e-mail est: "+email+ " \n et votre mot de passe est: "+mot_de_passe+" \n. Veuillez les garder confidentiels. \nVous pouvez désormais commencer à réserver des voitures via notre site Web ou notre application mobile. Il vous suffit de vous connecter avec votre adresse e-mail et votre mot de passe. \n Nous proposons une large gamme de voitures à choisir, vous êtes donc sûr de trouver la voiture parfaite pour vos besoins. Nous avons également des tarifs compétitifs et des conditions de \nlocation flexibles. \n Nous espérons que vous apprécierez notre service ! \n Sincèrement,La Société de réservation de voitures "
                    send_mail(
                        sujet,  
                        message1, 
                        email1,  
                        [email],  
                        fail_silently=False
                    )
                    return  Response({'Reponse':'Success', 'id':client.id})
                else:
                    return Response({'Reponse':'error'})
        except:
            pass
            return Response({'Reponse':'Faild'})
      
class InserClientTranfer(APIView):
    def post(self, request):
        try:
            nomprenom = request.POST['nomprenom']
            cin = request.POST['cin']
            paye = request.POST['paye']
            numerorue = request.POST['numerorue']
            telephone = request.POST['telephone']
            ville = request.POST['ville']
            region = request.POST['region']
            email = request.POST['email']
            token = request.POST['token']
            mot_de_passe = generate_crypte_id()
            photo_cin_passport= request.FILES['photo_cin_passport']
            photo = request.FILES.get('photo', None)
            nb = Client.objects.filter(email=email).count()
            if(nb==1):
                return  Response({'Reponse':'email déjà utilisé'})
            else:
                mot_de_passe2=make_password(mot_de_passe)
                if(photo==None):
                    client = Client(
                        nomprenom=nomprenom,
                        cin_passport=cin,
                        paye=paye,
                        numerorue=numerorue,
                        telephone=telephone,
                        ville=ville,
                        region=region,
                        email=email,
                        mot_de_passe=mot_de_passe2,
                        photo_cin_passport=photo_cin_passport,
                        statutClient="Activated",
                        token=token,
                        )
                else:
                    client = Client(
                        nomprenom=nomprenom,
                        cin_passport=cin,
                        paye=paye,
                        numerorue=numerorue,
                        telephone=telephone,
                        ville=ville,
                        region=region,
                        email=email,
                        mot_de_passe=mot_de_passe2,
                        photo_cin_passport=photo_cin_passport,
                        statutClient="Activated",
                        token=token,
                        photo=photo
                        )
                client.save()
                if (client):
                    sujet1 = " Bienvenue a Neapolis car",
                    sujet=sujet1
                    email1 = 'wassim.amdouni28@gmail.com'  
                    message1 = " Cher "+nomprenom+", \n Bienvenue à la Société de réservation de voitures ! Nous sommes ravis de vous compter parmi nos membres. \n Votre adresse e-mail est: "+email+ " \net votre mot de passe est: "+mot_de_passe+" \nVeuillez les garder confidentiels. \nVous pouvez désormais commencer à réserver des voitures via notre site Web ou notre application mobile. Il vous suffit de vous connecter avec votre adresse e-mail et votre mot de passe. \n Nous proposons une large gamme de voitures à choisir, vous êtes donc sûr de trouver la voiture parfaite pour vos besoins. Nous avons également des tarifs compétitifs et des conditions de \nlocation flexibles. \n Nous espérons que vous apprécierez notre service ! \n Sincèrement,La Société de réservation de voitures "
                    send_mail(
                        sujet,  
                        message1, 
                        email1,  
                        [email],  
                        fail_silently=False
                    )
                    return  Response({'Reponse':'Success','id':client.id})
                else:
                    return Response({'Reponse':'error'})
        except:
            pass
            return Response({'Reponse':'Faild'})
                        
class Effect_paiment(APIView):
    def post(self, request):
        try:
            body = json.loads(request.body.decode('utf-8'))
            id_cl = body.get('id')
            amount = str(body.get('amount')*1000)
            token = body.get('token')
            description = body.get('description')
            client = Client.objects.filter(id=id_cl).first()
            telephone = str(client.telephone)
            url = "https://api.preprod.konnect.network/api/v2/payments/init-payment"
            walletId = "64ce7fde5b47f30adb54f88a"
            api_key = "64ce7fde5b47f30adb54f887:o7n18DUWxmOnhiobjdMwG"
            headers = {
                "Content-Type": "application/json",
                "x-api-key": api_key
            }
            data = {
                "receiverWalletId": walletId,
                "token": token,
                "amount": amount,
                "type": "immediate",
                "description": description,
                "acceptedPaymentMethods": ["bank_card"],
                "lifespan": 10,
                "checkoutForm": False,
                "addPaymentFeesToAmount": False,
                "firstName": client.nomprenom,
                "lastName": client.nomprenom,
                "phoneNumber": telephone,
                "email": client.email,
                "orderId": "1234657",
                "webhook": "https://merchant.tech/api/notification_payment",
                "silentWebhook": True,
                "successUrl": "https://dev.konnect.network/gateway/payment-success",
                "failUrl": "https://dev.konnect.network/gateway/payment-failure",
                "theme": "light"
            }
            try:
                response = requests.post(url, headers=headers, data=json.dumps(data))
                response_data = response.json()
                return Response({'Reponse':'Success' ,"data": response_data})
            except requests.exceptions.RequestException as e:
                # Handle any errors that occurred during the request
                print(f"Error: {e}")
                return Response({'Reponse':'error'})
        except:
            pass
            return Response({'Reponse':'Faild'})
      
        
class InsertPiaemnt(APIView):
    def post(self , request):
        try:
            body= json.loads(request.body.decode('utf-8'))
            prix= body.get('prix',None)
            id_client = body.get('id',None)
            type= body.get('type',None)
            id_demande = body.get('id_demande', None)
            today = date.today()
            #date1 = today.strftime("%Y-%m-%d %H:%M:%S") //KeyError
            paiment= Paiment(prix=prix , type=type ,date=today, id_client_id=id_client , id_demande_id=id_demande )
            paiment.save()
            if(paiment):
                return Response({'Reponse':'Success'})
            else:
                return Response({'Reponse':'error'})
        except:
            pass
            return Response({'Reponse':'Faild'})
      
        
def sendNotifications(type):
    admins = Admin.objects.all()
    tokens = []
    admins=Admin.objects.all()
    for admin in admins:
        tokens.append(admin.token)
    message = messaging.MulticastMessage(
            notification=messaging.Notification(
                title="Noveau "+type,
                body="Noveau "+type+" insert"
            ),
            tokens=tokens,
         )
    response = messaging.send_multicast(message)

class Insert_reservation(APIView):
    def post(self, request):
        try:   
            body = json.loads(request.body.decode('utf-8'))
            nb_bagage  = body.get('nb_bagage', None)
            type = body.get('type')
            etat= body.get('etat')
            date_depar = body.get('dateRamasser')
            bureau_predre_la_voiture = body.get('location_de_rammaser')
            bureau_deposer_la_voiture = body.get('location_de_revenir')
            date_arriver = body.get('dateRevenir')
            numero_series = body.get('numeroSeries')
            id_client = body.get('id_Client')
            PLEIN_SSENCE=body.get('PLEIN ESSENCE')
            DEUXIEME_CONDUCTEUR = body.get('DEUXIÈME CONDUCTEUR')
            REHAUSSEUR = body.get('REHAUSSEUR ( 24-42 MOIS)')
            SYSTEME_DE_NAVIGATION_GPS = body.get('SYSTÈME DE NAVIGATION GPS')
            SIEGE_BEBE= body.get('SIÈGE BÉBÉ ( 6-24 MOIS)')
            today = date.today()
            demande = Demande(type=type , etat=etat , id_client_id= id_client)
            demande.save()
            id = demande.id
            if(demande):
                reservation= Reservation(date_depar=date_depar ,
                                        bureau_predre_la_voiture=bureau_predre_la_voiture ,
                                        bureau_deposer_la_voiture=bureau_deposer_la_voiture ,
                                        date_arriver =date_arriver,
                                        numero_series_id=numero_series,
                                        id_demande_id= id )
                reservation.save()
                id_reservation = reservation.id
                if(reservation):
                    if(PLEIN_SSENCE==True):
                        service1= Service(nom="PLEIN ESSENCE",
                                                descreptions="PLEIN ESSENCE",
                                                prix=120 ,
                                                id_demande_id =id)
                        service1.save()
                    if(DEUXIEME_CONDUCTEUR==True):
                        service2=Service(nom="DEUXIÈME CONDUCTEUR",
                                                descreptions="DEUXIÈME CONDUCTEUR",
                                                prix=0,
                                                id_demande_id=id)    
                        service2.save()
                    if(REHAUSSEUR==True):
                        service3=Service(
                                            nom="REHAUSSEUR ( 24-42 MOIS)",
                                            descreptions="REHAUSSEUR ( 24-42 MOIS)",
                                            prix=0,
                                            id_demande_id=id)
                        service3.save()
                    if(SYSTEME_DE_NAVIGATION_GPS==True):
                        service4= Service(
                                            nom="SYSTÈME DE NAVIGATION GPS",
                                            descreptions="SYSTÈME DE NAVIGATION GPS",
                                            prix=0,
                                            id_demande_id=id)
                        service4.save()
                    if(SIEGE_BEBE==True):
                        service5= Service(
                                            nom="SIÈGE BÉBÉ ( 6-24 MOIS)",
                                            descreptions="SIÈGE BÉBÉ ( 6-24 MOIS)",
                                            prix="0",
                                            id_demande_id=id)
                        service5.save()
                    sendNotifications("Reservations")
                    return Response({'Reponse':'Success', 'id':id})
                else:
                    return Response({'Reponse':'error'})
                sendNotifications("Reservations")
                return Response({'Reponse':'Success', 'id':id})
            else:
                return Response({'Reponse':'error'})
        except:
            pass
            return Response({'Reponse':'Faild'})
      
class Insert_transfer(APIView):
    def post(self, request):
        try:
            body = json.loads(request.body.decode('utf-8'))
            type = body.get('type')
            etat= body.get('etat')
            date_depar = body.get('date_de_depart')
            id_ListTransfer=body.get('idlisttransfer')
            numero_series = body.get('numeroSeries')
            id_client = body.get('id_Client')
            allez_retour=body.get('allez_retour')
            SIEGE_BEBE= body.get('SIÈGE BÉBÉ ( 6-24 MOIS)')
            demande = Demande( type=type , etat=etat , id_client_id= id_client)
            demande.save()
            id= demande.id
            if demande:
                transfer = Transfer(
                                    date_depar=date_depar,
                                    id_ListTransfer_id=id_ListTransfer,
                                    numero_series_id=numero_series,
                                    id_demande_id=id)
                transfer.save()
                id_transfer=transfer.id
                if transfer:
                    if (allez_retour == True):
                        service = Service(
                                        nom="allez et retour",
                                        descreptions="allez et retour",
                                        prix=0,
                                        id_demande_id=id)
                        service.save()
                    if(SIEGE_BEBE == True):
                        service2 = Service(
                                            nom="SIÈGE BÉBÉ ( 6-24 MOIS)",
                                            descreptions="SIÈGE BÉBÉ ( 6-24 MOIS)",
                                            prix="0",
                                            id_demande_id=id
                                            )
                        service2.save()
                    sendNotifications("Transfer")
                    return Response({'Reponse':'Success', 'id':id})
                else:
                    return Response({'Reponse':'error'})
                sendNotifications("Transfer")
                return Response({'Reponse':'Success', 'id':id})
            else:
                return Response({'Reponse':'error'})
        except:
            pass
            return Response({'Reponse':'Faild'})
      
class Insert_exurcion(APIView):
    def post(self, request):
        try:
            body = json.loads(request.body.decode('utf-8'))
            type = body.get('type')
            etat= body.get('etat')
            date_depar = body.get('date_de_depart')
            id_ListExucion= body.get('idlistexurion')
            numero_series = body.get('numeroSeries')
            id_client = body.get('id_Client')
            SIEGE_BEBE= body.get('SIÈGE BÉBÉ ( 6-24 MOIS)')
            demande = Demande( type=type  , etat=etat , id_client_id= id_client)
            demande.save()
            id= demande.id
            if(demande):
                exurcion= Exurcion(
                                        date_depar=date_depar ,
                                        id_ListExurcion_id=id_ListExucion,
                                        numero_series_id=numero_series,
                                        id_demande_id= id )
                exurcion.save()
                id_exurion =exurcion.id
                if(exurcion):
                    if(SIEGE_BEBE==True):
                        service= Service(
                                            nom="SIÈGE BÉBÉ ( 6-24 MOIS)",
                                            descreptions="SIÈGE BÉBÉ ( 6-24 MOIS)",
                                            prix="0",
                                            id_demande_id=id)
                        service.save()
                    sendNotifications("Exucion")
                    return Response({'Reponse':'Success', 'id':id})
                else:
                        return Response({'Reponse':'error'})
                sendNotifications("Exucion")
                return Response({'Reponse':'Success', 'id':id})
            else:
                return Response({'Reponse':'error'})
        except:
            pass
            return Response({'Reponse':'Faild'})
      

class InserAnnulation(APIView):
    def post(self, request ):
        try:
            body = json.loads(request.body.decode('utf-8'))
            id_cleint = body.get('id')
            id_demande = body.get('id_demande')
            descriptions = body.get('descriptions')
            annulation= Annulation(description=descriptions  , id_demande_id=id_demande)
            annulation.save()
            id=annulation.id
            if(annulation):
                demande= Demande.objects.get(id=id_demande)
                demande.etat="annule"
                demande.save()
                if demande :
                    sendNotifications("Annulation")
                    return Response({'Reponse':'Success'})
                else:
                    return Response({'Reponse':'error'})
            else:
                return Response({'Reponse':'error'})
        except:
            pass
            return Response({'Reponse':'Faild'})
      

class SendNotificationClient(APIView):
    def post(self, request):
         tokens_queryset = Client.objects.all()
         tokens = [token.token for token in tokens_queryset.token]
         message = messaging.MulticastMessage(
            notification=messaging.Notification(
                title="Notification Title",
                body="Notification Body"
            ),
            tokens=tokens,
         )

        # Send the message
         response = messaging.send_multicast(message)

        # Handle the response as needed
         return Response("send")
           
class Verification(APIView):
    def post(self,request ):
     try:
            body = json.loads(request.body.decode('utf-8'))
            email1 = body.get('email',None)
            mot_de_passe1 = body.get('mot_de_passe',None)
            client = Client.objects.filter(email=email1).first()
            nb= Client.objects.filter(email=email1).count()
            if(nb==1):
                checkpassword= check_password(mot_de_passe1 ,client.mot_de_passe)
                if(checkpassword):
                    if client.statutClient=="Activated":
                        id=Client.objects.filter(email=email1).first().id
                        return Response({'Response': 'Activated', 'id':id})
                    else:
                        return Response({'Response': 'Deactivated'})
                else:
                    return Response({'Response': 'Password Incorrect'})
            else:
                return Response({'Response': 'Not Exist'})
     except:
            pass
            return Response({'Reponse':'Faild'})

class AfficherListTransfer(APIView):
    def post(self , request , format=None):
        try:
            listTransfer= ListTransfer.objects.all()
            listtransfer_serializer= ListTransferSerializer(listTransfer , many=True)
            if(listtransfer_serializer!=None):
                return Response({'Reponse':'Success','data':listtransfer_serializer.data})
            else:
                return Response({'Response': 'Not Exist'})
        except:
            pass
            return Response({'Reponse':'Faild'})
      

class AfficherListExurcion(APIView):
    def post(self , request , format=None):
        try:
            listexurcion= ListExurcion.objects.all()
            listexurcion_serializer= ListExurcionSerializer(listexurcion , many=True)
            if(listexurcion_serializer!=None):
                return Response({'Reponse':'Success','data':listexurcion_serializer.data})
            else:
                return Response({'Response': 'Not Exist'})
        except:
            pass
            return Response({'Reponse':'Faild'})
      

class AfficherListTransfer1(APIView):
    def post(self , request , format=None):
        try:
            body = json.loads(request.body.decode('utf-8'))
            id = body.get('id', None)
            listTransfer= ListTransfer.objects.filter(id=id)
            listtransfer_serializer= ListTransferSerializer(listTransfer , many=True)
            if(listtransfer_serializer!=None):
                return Response({'Reponse':'Success','data':listtransfer_serializer.data})
            else:
                return Response({'Response': 'Not Exist'})
        except:
            pass
            return Response({'Reponse':'Faild'})
      

class AfficherListExurcion1(APIView):
    def post(self , request , format=None):
        try:
            body = json.loads(request.body.decode('utf-8'))
            id = body.get('id', None)
            listexurcion= ListExurcion.objects.filter(id=id)
            listexurcion_serializer= ListExurcionSerializer(listexurcion , many=True)
            if(listexurcion_serializer!=None):
                return Response({'Reponse':'Success','data':listexurcion_serializer.data})
            else:
                return Response({'Response': 'Not Exist'})
        except:
            pass
            return Response({'Reponse':'Faild'})
      

class Afficher_Gallery(APIView):
    def post(self , request , format=None):
        try:
            gallery=Gallery.objects.all()
            gallerySerializer= GallerySerializer(gallery , many=True)
            if(gallerySerializer!=None):
                return Response({'Reponse':'Success','data':gallerySerializer.data})
            else:
                return Response({'Response': 'Not Exist'})
        except:
            pass
            return Response({'Reponse':'Faild'})
      
    
def EtatVoiture(modele ,date1 ):
    voitures = Voiture.objects.filter(modele=modele)
    for voiture in voitures :
        car_reservion = Reservation.objects.filter(
                    numero_series__numero_series=voiture.numero_series,
                    date_depar__lte=date1,
                    date_arriver__gte=date1
                    ).exists()
        car_transfer = Transfer.objects.filter(
                            numero_series__numero_series=voiture.numero_series,
                            date_depar=date1,
                            ).exists()
        car_exucrion = Exurcion.objects.filter(
                            numero_series__numero_series=voiture.numero_series,
                            date_depar=date1,
                            ).exists()
        if (car_reservion!=True and  car_transfer!=True and car_exucrion!=True):
                return "disponible"
    else:
        return "No disponible"
    
def GroupByModele(voitures):
    voiture = []
    model=""
    for item in voitures:
        if model != item.modele :
            model= item.modele
            voiture.append(item)
    return voiture
            
class Afficher_demande_Client(APIView):
    def post(self, request):
        try:
            body = json.loads(request.body.decode('utf-8'))
            id = body.get('id', None)
            today = date.today()
            Demandes = []
            demandes = Demande.objects.filter(id_client=id).exclude(etat="annule")
            for demande1 in demandes:
                reservation = Reservation.objects.filter(
                                    id_demande_id=demande1.id,
                                    date_depar__lte=today,
                                    date_arriver__gte=today
                                    ).exists()
                transfer = Transfer.objects.filter(
                                id_demande_id=demande1.id,
                                date_depar__lte=today,
                                ).exists()
                exurcion = Exurcion.objects.filter(
                                id_demande_id=demande1.id,
                                date_depar__lte=today,
                                ).exists()
                reservation1  = Reservation.objects.filter(
                                    id_demande_id=demande1.id,
                                    date_arriver__lt=today,  
                                ).exists()
                transfer1 = Transfer.objects.filter(
                                id_demande_id=demande1.id,
                                date_depar__lte=today
                                ).exists()
                exurcion1 = Exurcion.objects.filter(
                                id_demande_id=demande1.id,
                                date_depar__lte=today,
                                ).exists()
                if(reservation or transfer or exurcion):
                        etat="en cours"
                elif(reservation1 or transfer1 or exurcion1) :
                        etat="Termine"
                else:
                        etat="en attend"
                if demande1.type == "Reservation":
                    reservation = Reservation.objects.filter(id_demande_id=demande1.id).first()
                    paiment = Paiment.objects.filter(id_demande_id=demande1.id).first()
                    voiture = Voiture.objects.filter(numero_series=reservation.numero_series_id).first()
                    details = {
                        "id": demande1.id,
                        "type": demande1.type,
                        "photo": voiture.photo.url if voiture.photo else None,
                        "modele": voiture.modele,
                        "prix": paiment.prix,
                        "etat": etat,
                        "date_de_depart": reservation.date_depar,
                        "date_de_revinier": reservation.date_arriver,
                        "date": demande1.date,
                    }
                    Demandes.append(details)
                elif demande1.type == "Transfer":
                    transfer = Transfer.objects.filter(id_demande_id=demande1.id).first()
                    lsTransfer = ListTransfer.objects.filter(id=transfer.id_ListTransfer_id).first()
                    voiture = Voiture.objects.filter(numero_series=transfer.numero_series_id).first()
                    paiment = Paiment.objects.filter(id_demande=demande1.id).first()
                    details = {
                        "id": demande1.id,
                        "type": demande1.type,
                        "photo": voiture.photo.url if voiture.photo else None,
                        "modele": voiture.modele,
                        "prix": paiment.prix,
                        "etat": etat,
                        "date_de_depart":transfer.date_depar,
                        "address_depart": lsTransfer.address_depart,
                        "address_fin": lsTransfer.address_fin,
                        "date": demande1.date,
                    }
                    Demandes.append(details)
                elif demande1.type == "Exurcion":
                    exurcion = Exurcion.objects.filter(id_demande=demande1.id).first()
                    print(demande1.id)
                    lsExurcion = ListExurcion.objects.filter(id=exurcion.id_ListExurcion_id).first()
                    voiture = Voiture.objects.filter(numero_series=exurcion.numero_series_id).first()
                    paiment = Paiment.objects.filter(id_demande=demande1.id).first()
                    details = {
                        "id": demande1.id,
                        "type": demande1.type,
                        "photo": voiture.photo.url if voiture.photo else None,
                        "modele": voiture.modele,
                        "prix": paiment.prix,
                        "etat": etat,
                        "date_de_depart": exurcion.date_depar,
                        "address_depart": lsExurcion.address_depart,
                        "date": demande1.date,
                    }
                    Demandes.append(details)
            if(Demandes!=None):
                return Response({'Reponse':'Success','data':Demandes})
            else:
                return Response({'Reponse': 'Not Exist'})      
        except:
            pass
            return Response({'Reponse':'Faild'})
      
class Afficher_Voitures1(APIView):
    def post(self, request , ):
        try:
            body = json.loads(request.body.decode('utf-8'))
            nb_bagage  = body.get('nb_bagage', None)
            date1 = body.get('date', None) 
            print(nb_bagage , date1)
            List_Voitures=[]
            voiture1 = Voiture.objects.filter(nb_bags__gte=nb_bagage)
            voitures=GroupByModele(voiture1)
            for voiture in voitures:
                voiture1 = {
                "numero_series": voiture.numero_series,
                "modele": voiture.modele,
                "nb_seats":voiture.nb_seats,
                "nb_bags":voiture.nb_bags,
                "nb_ports":voiture.nb_ports,
                "prix_jour":voiture.prix_jour,
                "caution":voiture.caution,
                "annee":voiture.annee,
                "etat":voiture.etat,
                "marque": Marquer.objects.filter(id=voiture.id_marquer_id).first().nom,
                "photoMarque":Marquer.objects.filter(id=voiture.id_marquer_id).first().logo,
                "photo":voiture.photo,
                "description":voiture.description,
                "boite":voiture.boite,
                "class_voiture":voiture.class_voiture,
                "id_marquer":voiture.id_marquer,
                "disponibilite" : EtatVoiture(voiture.modele, date1),
                }
                List_Voitures.append(voiture1)
            serializer = VoituresSerializer(List_Voitures, many=True)
            if(serializer!=None):
                return Response({'Reponse':'Success','data':serializer.data})
            else:
                return Response({'Reponse': 'Not Exist'})   
        except:
            pass
            return Response({'Reponse':'Faild'})
      
class Afficher_Voitures(APIView):
    def post(self , request , format=None):
        try:
            body = json.loads(request.body.decode('utf-8'))
            voitures = Voiture.GroupByModele()
            date1 = body.get('date', None) 
            List_Voitures=[]
            for voiture in voitures:
                    voiture1 = {
                    "numero_series": voiture.numero_series,
                    "modele": voiture.modele,
                    "nb_seats":voiture.nb_seats,
                    "nb_bags":voiture.nb_bags,
                    "nb_ports":voiture.nb_ports,
                    "prix_jour":voiture.prix_jour,
                    "caution":voiture.caution,
                    "annee":voiture.annee,
                    "etat":voiture.etat,
                    "marque": Marquer.objects.filter(id=voiture.id_marquer_id).first().nom,
                    "photoMarque":Marquer.objects.filter(id=voiture.id_marquer_id).first().logo,
                    "photo":voiture.photo,
                    "description":voiture.description,
                    "boite":voiture.boite,
                    "class_voiture":voiture.class_voiture,
                    "id_marquer":voiture.id_marquer,
                    "disponibilite" : EtatVoiture(voiture.modele , date1),
                    }
                    List_Voitures.append(voiture1)
                    serializer = VoituresSerializer(List_Voitures, many=True)
            if(serializer!=None):
                return Response({'Reponse':'Success','data':serializer.data})
            else:
                return Response({'Reponse': 'Not Exist'})   
        except:
            pass
            return Response({'Reponse':'Faild'})
       
     
class getNumeroSeries(APIView):
    def post(self , request , format=None):
      try:
        body = json.loads(request.body.decode('utf-8'))
        modele = body.get('modele', None) 
        date1 = body.get('date', None)    
        voitures = Voiture.objects.filter(modele=modele)
        for voiture in voitures:
                car_reservion = Reservation.objects.filter(
                                numero_series__numero_series=voiture.numero_series,
                                date_depar__lte=date1,
                                date_arriver__gte=date1
                                ).exists()
                car_transfer = Transfer.objects.filter(
                                numero_series__numero_series=voiture.numero_series,
                                date_depar=date1,
                                ).exists()
                car_exucrion = Exurcion.objects.filter(
                                numero_series__numero_series=voiture.numero_series,
                                date_depar=date1,
                                ).exists()
                if(car_reservion!=True and  car_transfer!=True and car_exucrion!=True):
                     return Response({'Reponse':'Success','numerSeries':voiture.numero_series})
                else :
                    return Response({'Reponse': 'Not Exist'})  
        return Response({'Reponse':'error','etat':'no diponible'})
      except:
            pass
            return Response({'Reponse':'Faild'})
      
class Afficher_Client(APIView):
    def post(self, request, format=None):
        try:
            body = json.loads(request.body.decode('utf-8'))
            id = body.get('id')
            clients = Client.objects.filter(id=id)
            if clients.first().statutClient=="Activated":
                clients_serializer = ClientSerializer(clients, many=True)
                if(clients_serializer.data!=None):
                    return Response({'Reponse':'Success','data':clients_serializer.data})
                else:
                    return Response({'Reponse': 'Not Exist'})  
            else:
                 return Response({'Response': 'Deactivated'})
        except:
            pass
            return Response({'Reponse':'Faild'})
      
    
class Afficher_OptionVoitures(APIView):
    def post(self , request , format=None):
        try:
            body = json.loads(request.body.decode('utf-8'))
            numeroSeries = body.get('numeroSeries')
            options = Options.objects.filter(numero_series_id= numeroSeries)
            serialize = OptionsSerializer(options , many=True)
            if(serialize!=None):
                return Response({'Reponse':'Success','data':serialize.data})
            else:
                return Response({'Reponse': 'Not Exist'})   
        except:
            pass
            return Response({'Reponse':'Faild'})
      
class Afficher_Post(APIView):
    def post(self,request):
        try:
            post = Post.objects.all()
            serializer = PostSerializer(post, many=True)
            if(serializer.data!=None):
                return Response({'Reponse':'Success','data':serializer.data})
            else:
                return Response({'Reponse': 'Not Exist'})   
        except:
            pass
            return Response({'Reponse':'Faild'})
      
    
class UpadateClientPassword(APIView):
   def post(self,request):
      try:
         body = json.loads(request.body.decode('utf-8'))
         id1  = body.get('id',None)
         mot_de_passe1 = body.get('mot_de_passe',None)
         mot_de_passe2 = body.get('nmot_de_passe',None)
         mot_de_passe3=make_password(body.get('nmot_de_passe',None))
         client= Client.objects.get(id=id1)
         checkpassword= check_password(mot_de_passe1 ,client.mot_de_passe)
         if(checkpassword):
            client.mot_de_passe=mot_de_passe3
            client.save()
            return Response({'Reponse':'Success'})
         else:
             return Response({'Reponse':'verife mot de passe'})
      except:
            pass
            return Response({'Reponse':'Faild'})
      
class ContinueInscriClient(APIView):
    def post(self , request):
        try:
            client_id = request.POST['id']
            numeroparmis = request.POST['numeroparmis']
            nomentrprise = request.POST['nomentrprise']
            photo_parmis=request.FILES['photo_parmis']
            client = Client.objects.get(id=client_id)
            client.numeroparmis=numeroparmis
            client.nomentrprise=nomentrprise
            client.photo_parmis=photo_parmis
            client.save()
            if(client):
                return  Response({'Reponse':'Success'})
            else:
                return Response({'Reponse':'error'})
        except:
            pass
            return Response({'Reponse':'Faild'})
      
class UpdateClient(APIView):
    def post(self, request):
        try:
            client_id = request.POST['id']
            telephone = request.POST['telephone']
            email = request.POST['email']
            client = Client.objects.get(id=client_id)
            client.telephone = telephone
            client.email = email
            client.save()
            if(client):
                return Response({'Reponse':'Success'})
            else:
                return Response({'Reponse': 'Failed'})
        except:
            pass
        return Response({'Reponse': 'Failed'})



#----------------------------------------------------------------------------------
#---------------------------------------------------------------------

def generate_code_verification(admin,opt):
    code=0
    email=admin.email
    password=admin.mot_de_passe
    for i in range(len(email)):
        code=code+ ord(email[i])

    for i in range(len(password)):
        code=code+ ord(password[i])

    for i in range(len(opt)):
        code=code+ ord(opt[i])
    
    date=datetime.now()

    y=(code // 10)+int(date.strftime("%Y"))+int(date.strftime("%H"))
    m=(code // 10)+int(date.strftime("%m"))+int(date.strftime("%H"))
    d=(code // 10)+int(date.strftime("%d"))+int(date.strftime("%H"))
    code=code+y+m+d
    while(code>9999):
        code=code/10
    return code


def sendNotificationForAdmin(title,body,dataObject=None):
    tokens=[]
    admins=Admin.objects.all()
    for admin in admins:
        tokens.append(admin.token)

    message = messaging.MulticastMessage(
        notification=messaging.Notification(
            title=title,
            body=body
        ),
        data=dataObject,
        tokens=tokens,
    )
    # Send the message
    response = messaging.send_multicast(message)

def sendNotificationForClient(title,body,dataObject=None):
    tokens=[]
    clients=Client.objects.all()
    for client in clients:
        tokens.append(client.token)

    message = messaging.MulticastMessage(
        notification=messaging.Notification(
            title=title,
            body=body
        ),
        data=dataObject,
        tokens=tokens,
    )
    # Send the message
    response = messaging.send_multicast(message)

#Login Admin
class Login_Admin(APIView):
    def post(self, request):
        try:
            gemail = request.POST['email']
            gpassword = request.POST['password']
                
            if (Admin.objects.filter(email=gemail).exists()):
                if(Admin.objects.filter(email=gemail,mot_de_passe=gpassword).exists()):
                    if(Admin.objects.filter(email=gemail,mot_de_passe=gpassword,statutAdmin='Activated').exists()):
                        a=Admin.objects.filter(email=gemail,mot_de_passe=gpassword).first()
                        code=generate_code_verification(a,"check_login")
                        body="Entrez le code à 4 chiffres ci-dessous pour vérifier votre identité et retrouver l’accès à votre compte Neapolic.\n\n{}\n\nMerci de nous aider à sécuriser votre compte. L’équipe Neapolic".format(code)
                        send_mail(
                                "Voici votre code de vérification {}".format(code), 
                                body,
                                settings.EMAIL_HOST_USER, [a.email,])
                        return Response({'Response': 'Activated'})
                    return Response({'Response': 'Deactivated'})
                return Response({'Response': 'Password Incorrect'})
            return Response({'Response': 'Not Exist'})

        except:
            return Response({'Response': 'Failed'})
        
class Validation_Login(APIView):
    def post(self, request):
        try:
            gemail = request.POST['email']
            gpassword = request.POST['password']
            gcode = int(request.POST['code'])
            gtoken = request.POST['token']
            if(Admin.objects.filter(email=gemail,mot_de_passe=gpassword,statutAdmin='Activated').exists()):
                admin=Admin.objects.filter(email=gemail,mot_de_passe=gpassword).first()  

                if (gcode==generate_code_verification(admin,"check_login")):
                    admin.token=gtoken
                    admin.save()
                    serialized_obj = serializers.serialize('json',[admin,])
                    return Response({'Response': 'Success',"Admin":serialized_obj})
                return Response({'Response': 'Not Correct'})
            return Response({'Response': 'Deactivated'})
        except:
            return Response({'Response': 'Failed'})
        
class Resend_Code_Login(APIView):
    def post(self, request):
        try:
            
            gemail = request.POST['email']
            gpassword = request.POST['password']  
            a=Admin.objects.filter(email=gemail,mot_de_passe=gpassword).first()
            if(Admin.objects.filter(email=gemail,mot_de_passe=gpassword,statutAdmin='Activated').exists()):
                code=generate_code_verification(a,"check_login")
                body="Entrez le code à 4 chiffres ci-dessous pour vérifier votre identité et retrouver l’accès à votre compte Neapolic.\n\n{}\n\nMerci de nous aider à sécuriser votre compte. L’équipe Neapolic".format(code)
                send_mail(
                        "Voici votre code de vérification {}".format(code), 
                        body,
                        settings.EMAIL_HOST_USER, [a.email,] )
                return Response({'Response': 'Success'})
            return Response({'Response': 'Deactivated'})
        except:
            return Response({'Response': 'Failed'})

class Test_Login_Admin(APIView):
    def post(self, request):
        try:
            gemail = request.POST['email']
            gpassword = request.POST['password']
                
            if(Admin.objects.filter(email=gemail,mot_de_passe=gpassword,statutAdmin='Activated').exists()):
                return Response({'Response': 'Success'})
            return Response({'Response': 'Failed'})

        except:
            return Response({'Response': 'Failed'})
                 
#Forget Password Admin

class Forget_Password_Admin(APIView):
    def post(self, request):
        try:
            gemail = request.POST['email']  
            if (Admin.objects.filter(email=gemail).exists()):
                if(Admin.objects.filter(email=gemail,statutAdmin='Activated').exists()):
                    a=Admin.objects.filter(email=gemail).first()
                    code=generate_code_verification(a,"check_forget_password")
                    body="Entrez ce code pour terminer la réinitialisation.\n{}\nSi vous n’avez pas demandé ce code, nous vous recommandons de modifier votre mot de passe Neapolic.".format(code)
                    send_mail(
                            "Voici votre code de réinitialisation {}".format(code), 
                            body,
                            settings.EMAIL_HOST_USER, [a.email,] )
                    return Response({'Response': 'Exist'})
                return Response({'Response': 'Deactivated'})                
            return Response({'Response': 'Not Exist'})

        except:
            return Response({'Response': 'Failed'})
        
class Validation_Forget_Password(APIView):
    def post(self, request):
        try:
            gemail = request.POST['email']
            gcode = int(request.POST['code'])
            if(Admin.objects.filter(email=gemail,statutAdmin='Activated').exists()):
                admin=Admin.objects.filter(email=gemail).first()  
                if (gcode==generate_code_verification(admin,"check_forget_password")):
                    serialized_obj = serializers.serialize('json',[admin,])
                    return Response({'Response': 'Success',"Admin":serialized_obj})
                return Response({'Response': 'Not Correct'})
            return Response({'Response': 'Deactivated'})  
        except:
            return Response({'Response': 'Failed'})
        
class Resend_Code_Forget_Password(APIView):
    def post(self, request):
        try:
            gemail = request.POST['email'] 
            if(Admin.objects.filter(email=gemail,statutAdmin='Activated').exists()):
                a=Admin.objects.filter(email=gemail,).first()
                code=generate_code_verification(a,"check_forget_password")
                body="Entrez ce code pour terminer la réinitialisation.\n{}\nSi vous n’avez pas demandé ce code, nous vous recommandons de modifier votre mot de passe Neapolic.".format(code)
                send_mail(
                        "Voici votre code de réinitialisation {}".format(code), 
                        body,
                        settings.EMAIL_HOST_USER, [a.email,] )
                return Response({'Response': 'Success'})
            return Response({'Response': 'Deactivated'})
        except:
            return Response({'Response': 'Failed'})

class New_Password_Admin(APIView):
    def post(self, request):
        try:
            gemail = request.POST['email']
            gnew_password = request.POST['new_password']    
            Admin.objects.filter(email=gemail).update(mot_de_passe=gnew_password)
            return Response({'Response': 'Success'})
        except:
            return Response({'Response': 'Failed'})
   
class Update_Admin(APIView):
    def post(self, request):
        try:
            gid = request.POST.get('id',None)
            gnom_prenom = request.POST.get('nom_prenom',None)   
            gtelephone = request.POST.get('telephone',None)
            gemail = request.POST.get('email',None)
            gmot_de_passe = request.POST.get('mot_de_passe',None)
            gconfirm_mot_de_passe = request.POST.get('confirm_mot_de_passe',None) 
            gphoto = request.FILES.get('photo',None) 

            a=Admin.objects.filter(id=gid,mot_de_passe=gconfirm_mot_de_passe).first()
            if(a!=None):
                if(gphoto!=None):
                    Admin.objects.filter(id=gid).update(
                        nom_prenom=gnom_prenom,
                        telephone=gtelephone,
                        email=gemail,
                        mot_de_passe=gmot_de_passe,
                        )
                    if(a.photo!="default_profile_picture.png"):
                        a.photo.delete()
                    a.photo=gphoto
                    a.save()
                    return Response({'Response': 'Success'})
                else:
                    Admin.objects.filter(id=gid).update(
                        nom_prenom=gnom_prenom,
                        telephone=gtelephone,
                        email=gemail,
                        mot_de_passe=gmot_de_passe
                        )
                    return Response({'Response': 'Success'})
            return Response({'Response': 'Incorrect Password'})
        except:
            return Response({'Response': 'Failed'})
   
#Get Model for Admin
class GetClient(APIView):
    def post(self, request):
        try:
            gidClient = request.POST['idClient']
            c=Client.objects.filter(id=gidClient).first()
            if(c!=None):
                serialized_obj = serializers.serialize('json',[c,])
                return Response({'Response': 'Success',"Client":serialized_obj})
            return Response({'Response': 'Not Exist'})
        except:
            return Response({'Response': 'Failed'})
   
class GetAdmin(APIView):
    def post(self, request):
        try:
            gidAdmin = request.POST['idAdmin']
            a=Admin.objects.filter(id=gidAdmin).first()
            if(a!=None):
                serialized_obj = serializers.serialize('json',[a,])
                return Response({'Response': 'Success',"Admin":serialized_obj})
            return Response({'Response': 'Not Exist'})
        except:
            return Response({'Response': 'Failed'})

class GetVoiture(APIView):
    def post(self, request):
        try:
            gidVoiture = request.POST['idVoiture']
            v=Voiture.objects.filter(numero_series=gidVoiture).first()
            if(v!=None):
                serialized_obj = serializers.serialize('json',[v,])
                return Response({'Response': 'Success',"Voiture":serialized_obj})
            return Response({'Response': 'Not Exist'})
        except:
            return Response({'Response': 'Failed'})

class GetDemande(APIView):
    def post(self, request):
        try:
            gidDemande = request.POST['idDemande']
            d=Demande.objects.filter(id=gidDemande).first()
            if(d!=None):
                serialized_obj = serializers.serialize('json',[d,])
                return Response({'Response': 'Success',"Demande":serialized_obj})
            return Response({'Response': 'Not Exist'})
        except:
            return Response({'Response': 'Failed'})

class GetReservation(APIView):
    def post(self, request):
        try:
            gidReservation = request.POST['idReservation']
            r=Reservation.objects.filter(id=gidReservation).first()
            if(r!=None):
                serialized_obj = serializers.serialize('json',[r,])
                return Response({'Response': 'Success',"Reservation":serialized_obj})
            return Response({'Response': 'Not Exist'})
        except:
            return Response({'Response': 'Failed'})

class GetMarquer(APIView):
    def post(self, request):
        try:
            gidMarquer = request.POST['idMarquer']
            m=Marquer.objects.filter(id=gidMarquer).first()
            if(m!=None):
                serialized_obj = serializers.serialize('json',[m,])
                return Response({'Response': 'Success',"Marquer":serialized_obj})
            return Response({'Response': 'Not Exist'})
        except:
            return Response({'Response': 'Failed'})

class GetService(APIView):
    def post(self, request):
        try:
            gidDemande = request.POST['idDemande']
            s=Service.objects.filter(id_demande=gidDemande).all()
            if(s!=None):
                serialized_obj = serializers.serialize('json',s)
                return Response({'Response': 'Success',"Services":serialized_obj})
            return Response({'Response': 'Not Exist'})
        except:
            return Response({'Response': 'Failed'})

class GetListTransfer(APIView):
    def post(self, request):
        try:
            gidListTransfer = request.POST['idListTransfer']
            lt=ListTransfer.objects.filter(id=gidListTransfer).first()
            if(lt!=None):
                serialized_obj = serializers.serialize('json',[lt,])
                return Response({'Response': 'Success',"ListTransfer":serialized_obj})
            return Response({'Response': 'Not Exist'})
        except:
            return Response({'Response': 'Failed'})



class GetGallery(APIView):
    def post(self, request):
        try:
            glistExurcion = request.POST['idlistExurcion']
            g=Gallery.objects.filter(listExurcion=glistExurcion).all()
            if(g!=None):
                serialized_obj = serializers.serialize('json',g)
                return Response({'Response': 'Success',"Gallerys":serialized_obj})
            return Response({'Response': 'Not Exist'})
        except:
            return Response({'Response': 'Failed'})

class InserGallery(APIView):
    def post(self, request):
        try:
            gtitle = request.POST.get('title', None)
            gphoto=  request.FILES.get('photo', None)
            
            gidListExurcion = request.POST.get('idListExurcion', None)
            le=ListExurcion.objects.filter(id=gidListExurcion).first()
            if(gtitle!=""):
                g=Gallery.objects.create(titleGallery=gtitle,listExurcion=le)
                if(gphoto!=None):
                    g.photo=gphoto
                return Response({'Response': 'Success'}) 
            return Response({'Response': 'Failed'})
        except:
            return Response({'Response': 'Failed'})

class DeleteGallery(APIView):
    def post(self, request):
        try:
            gid = request.POST.get('id', None)
            o=Gallery.objects.filter(idPhoto=gid).first()
            if(o!=None):
                Gallery.objects.filter(idPhoto=gid).delete()
                return Response({'Response': 'Success'}) 
            return Response({'Response': 'Failed'})
        except:
            return Response({'Response': 'Failed'})

class GetListExurcion(APIView):
    def post(self, request):
        try:
            gidListExurcion = request.POST['idListExurcion']
            le=ListExurcion.objects.filter(id=gidListExurcion).first()
            if(le!=None):
                serialized_obj = serializers.serialize('json',[le,])
                return Response({'Response': 'Success',"ListExurcion":serialized_obj})
            return Response({'Response': 'Not Exist'})
        except:
            return Response({'Response': 'Failed'})


#Api for Reservation Pages
class GetAllReservation(APIView):
    def post(self, request):
        try:
            r=Reservation.objects.all()
            if(r!=None):
                serialized_obj = serializers.serialize('json',r)
                return Response({'Response': 'Success',"Reservations":serialized_obj})
            return Response({'Response': 'Not Exist'})
        except:
            return Response({'Response': 'Failed'})

class SearchReservation(APIView):
    def post(self, request):

        try:
            gsearchValue = request.POST.get('searchValue', None)
            gdate_Start = request.POST.get('date_Start', None)#yyyy-MM-dd kk:mm __range
            gdate_End = request.POST.get('date_End', None)#yyyy-MM-dd kk:mm
            search01=Reservation.objects.all()
            searchStatue=False
        
            #search by rang date

            if(gdate_Start!="" and gdate_End!=""):
                date_Start=datetime.strptime(gdate_Start, "%Y-%m-%d %H:%M:%S")
                date_End=datetime.strptime(gdate_End, "%Y-%m-%d %H:%M:%S")
                search02=Reservation.objects.filter(date_depar__range=(date_Start,date_End)).all()
                if (len(search02)!=0):
                    search01=search02
                    searchStatue=True
                
                    #search by searchValue

                    if(gsearchValue!=""):
                        c=Client.objects.filter(nomprenom__contains=gsearchValue).all()
                        if(len(c)!=0):
                            d=Demande.objects.select_related('id_client').filter(id_client__in=c).all()
                            if(len(d)!=0):
                                search03=Reservation.objects.select_related('id_demande').filter(id_demande__in=d)
                                if(len(search03)!=0):
                                    search01=search01 & search03
                                    searchStatue=True
                                    

                        #Inner Join with Voiture
                        
                        v01 = Voiture.objects.filter(
                            Q(annee__contains=gsearchValue) |
                            Q(class_voiture__contains=gsearchValue) |
                            Q(modele__contains=gsearchValue)).all()
                        
                        m=Marquer.objects.filter(nom__contains=gsearchValue).all()
                        v02=[]
                        if(len(m)!=0):
                            v02=Voiture.objects.select_related('id_marquer').filter(id_marquer__in=m).all()
                        
                        
                        if(len(v01)!=0):
                            if(len(v02)!=0):
                                v03=v01 & v02
                            else:
                                v03=v01
                        else:
                            v03=v02
                        search04=Reservation.objects.select_related('numero_series').filter(numero_series__in=v03).all()
                        if(len(search04)!=0):
                            search01=search01 & search04
                            searchStatue=True
                            
                    
        
            if(searchStatue):
                serialized_obj = serializers.serialize('json',search01)
                return Response({'Response': 'Success',"Reservations":serialized_obj})
            return Response({'Response': 'Not Exist'})
        except:
            return Response({'Response': 'Failed'})

class Update_Etat_Demande(APIView):
    def post(self, request):
        
       
        gidReservation = request.POST['idReservation']
        getat = request.POST['etat']
        gprix = request.POST['prix']

        r=Reservation.objects.filter(id=gidReservation).first()
        if(r!=None):
            r.id_demande.etat=getat
            r.id_demande.save()
            if(getat=="Annuler"):
                Annulation.objects.create(date=datetime.now(),description='Admin annuler Cette Demande',id_demande=r.id_demande.id)
            if(getat=="En Cours"):
                Paiment.objects.create(prix=gprix,date=datetime.now(),type='Cash',id_client=r.id_demande.id_client,id_demande=r.id_demande)
            return Response({'Response': 'Success'})
        return Response({'Response': 'Not Exist'})
        try:
            pass
        except:
            return Response({'Response': 'Failed'})



#Api for Client Pages
class GetAllClient(APIView):
    def post(self, request):
        try:
            c=Client.objects.all()
            if(c!=None):
                serialized_obj = serializers.serialize('json',c)
                return Response({'Response': 'Success',"Clients":serialized_obj})
            return Response({'Response': 'Not Exist'})
        except:
            return Response({'Response': 'Failed'})

class SearchClient(APIView):
    def post(self, request):

        try:
            gsearchValue = request.POST.get('searchValue', None)
        
            if(gsearchValue!=""):
                c=Client.objects.filter(nomprenom__contains=gsearchValue).all()
                if(len(c)!=0):
                    serialized_obj = serializers.serialize('json',c)
                    return Response({'Response': 'Success',"Clients":serialized_obj})
            return Response({'Response': 'Not Exist'})
        except:
            return Response({'Response': 'Failed'})

class ActivateClient(APIView):
    def post(self, request):
        try:
            gidClient = request.POST.get('idClient', None)
            gstatutClient = request.POST.get('statutClient', None)
            if(gidClient!="" and (gstatutClient=="Activated" or gstatutClient=="Deactivated")):
                Client.objects.filter(id=gidClient).update(statutClient=gstatutClient)
                return Response({'Response': 'Success'}) 
            return Response({'Response': 'Failed'})
        except:
            return Response({'Response': 'Failed'})



#Api for Voiture Pages
class GetAllMarquer(APIView):
    def post(self, request):
        try:
            m=Marquer.objects.all()
            if(m!=None):
                serialized_obj = serializers.serialize('json',m)
                return Response({'Response': 'Success',"Marquers":serialized_obj})
            return Response({'Response': 'Not Exist'})
        except:
            return Response({'Response': 'Failed'})
  
class Insert_Update_Marquer(APIView):
    def post(self, request):
        gid = int(request.POST.get('id',None))
        gnom = request.POST.get('nom',None)
        glogo = request.FILES.get('logo',None)
        if(gid==0):
            if (Marquer.objects.filter(nom__contains=gnom).first()==None):
                if(glogo!=None):
                    m=Marquer.objects.create(nom=gnom,logo=glogo)
                else:
                    m=Marquer.objects.create(nom=gnom)
                serialized_obj = serializers.serialize('json',[m,])
                return Response({'Response': 'Success',"Marquer":serialized_obj})
            return Response({'Response': 'Exist'})
        else:
            m=Marquer.objects.filter(id=gid).first()
            if (m!=None):
                m.nom=gnom
                if(glogo!=None):
                    if(m.logo!="default_profile_picture.png"):
                        m.logo.delete()
                    m.logo=(glogo)            
                m.save()
                m=Marquer.objects.filter(id=gid).first()
                serialized_obj = serializers.serialize('json',[m,])
                return Response({'Response': 'Success',"Marquer":serialized_obj})
            return Response({'Response': 'Not Exist'})

        try:
            pass
        except:
            return Response({'Response': 'Failed'})
 
class GetAllVoiture(APIView):
    def post(self, request):
        try:
            v=Voiture.objects.all()
            if(v!=None):
                serialized_obj = serializers.serialize('json',v)
                return Response({'Response': 'Success',"Voitures":serialized_obj})
            return Response({'Response': 'Not Exist'})
        except:
            return Response({'Response': 'Failed'})

class SearchVoiture(APIView):
    def post(self, request):
        
        gsearchValue = request.POST.get('searchValue', None)
        #search by searchValue
        if(gsearchValue!=""):
            #Inner Join with Voiture
            v01=[]
            v02=[]
            v03=[]
            
            v01 = Voiture.objects.filter(
                Q(annee__contains=gsearchValue) |
                Q(class_voiture__contains=gsearchValue) |
                Q(modele__contains=gsearchValue)).all()
            
            m=Marquer.objects.filter(nom__contains=gsearchValue).all()
            if(len(m)!=0):
                v02=Voiture.objects.select_related('id_marquer').filter(id_marquer__in=m).all()
            
            if(len(v01)!=0):
                if(len(v02)!=0):
                    v03=v01 | v02
                else:
                    v03=v01
            else:
                if(len(v02)!=0):
                    v03=v02
                                    
    
            if(len(v03)!=0):
                serialized_obj = serializers.serialize('json',v03)
                return Response({'Response': 'Success',"Voitures":serialized_obj})
        return Response({'Response': 'Not Exist'})
        try:
            pass
        except:
            return Response({'Response': 'Failed'})

class GetOptions(APIView):
    def post(self, request):
        try:
            gidVoiture = request.POST['idVoiture']
            o=Options.objects.filter(numero_series=gidVoiture).all()
            if(o!=None):
                serialized_obj = serializers.serialize('json',o)
                return Response({'Response': 'Success',"Options":serialized_obj})
            return Response({'Response': 'Not Exist'})
        except:
            return Response({'Response': 'Failed'})

class InserVoiture(APIView):
    def post(self, request):
            
        try:
            gnumero_series = request.POST.get('numero_series',None)
            gmodele = request.POST.get('modele',None)
            gclass_voiture = request.POST.get('class_voiture',None)
            gannee = int(request.POST.get('annee',None))
            
            gboite = request.POST.get('boite',None)
            gnb_seats = int(request.POST.get('nb_seats',None))
            gnb_bags = int(request.POST.get('nb_bags',None))
            gnb_ports = int(request.POST.get('nb_ports',None))
            
            gcolor = request.POST.get('color',None)
            
            getat = request.POST.get('etat',None)
            gdescription = request.POST.get('description',None)
            
            gcaution= float(request.POST.get('caution',None))
            gprix_jour = float(request.POST.get('prix_jour',None))
            
            gphoto = request.FILES.get('photo',None)

            gid_marquer = request.POST.get('id_marquer',None)
            m=Marquer.objects.filter(id=gid_marquer).first()
            

            v01=Voiture.objects.filter(numero_series=gnumero_series).first()
            if(v01==None):
                if(gphoto!=None):
                    v=Voiture.objects.create(
                        numero_series=gnumero_series,
                        modele=gmodele,
                        class_voiture=gclass_voiture,
                        annee=gannee,

                        boite=gboite,
                        nb_seats=gnb_seats,
                        nb_bags=gnb_bags,
                        nb_ports=gnb_ports,

                        color=gcolor,

                        etat=getat,
                        description=gdescription,

                        caution=gcaution,
                        prix_jour=gprix_jour,

                        id_marquer=m
                    )
                    v.photo=gphoto
                    v.save()
                else:
                    v=Voiture.objects.create(
                        numero_series=gnumero_series,
                        modele=gmodele,
                        class_voiture=gclass_voiture,
                        annee=int(gannee),

                        boite=gboite,
                        nb_seats=gnb_seats,
                        nb_bags=gnb_bags,
                        nb_ports=gnb_ports,

                        color=gcolor,

                        etat=getat,
                        description=gdescription,

                        caution=gcaution,
                        prix_jour=gprix_jour,

                        id_marquer=m
                    )
                
                serialized_obj = serializers.serialize('json',[v,])
                return Response({'Response': 'Success',"Voiture":serialized_obj})
            return Response({'Response': 'Exist'})   
        except:
            return Response({'Response': 'Failed'})

class InserOption(APIView):
    def post(self, request):
        try:
            gtitle = request.POST.get('title', None)
            gdescriptions = request.POST.get('descriptions', None)
            gnumero_series = request.POST.get('numero_series', None)
            v=Voiture.objects.filter(numero_series=gnumero_series).first()
            if(gtitle!=""):
                Options.objects.create(title=gtitle,descriptions=gdescriptions,numero_series=v)
                return Response({'Response': 'Success'}) 
            return Response({'Response': 'Failed'})
        except:
            return Response({'Response': 'Failed'})

class DeleteOption(APIView):
    def post(self, request):
        try:
            gid = request.POST.get('id', None)
            o=Options.objects.filter(id=gid).first()
            if(o!=None):
                Options.objects.filter(id=gid).delete()
                return Response({'Response': 'Success'}) 
            return Response({'Response': 'Failed'})
        except:
            return Response({'Response': 'Failed'})

class UpdateVoiture(APIView):
    def post(self, request):
            
        try:
            gid=request.POST.get('id',None)
            gnumero_series = request.POST.get('numero_series',None)
            gmodele = request.POST.get('modele',None)
            gclass_voiture = request.POST.get('class_voiture',None)
            gannee = int(request.POST.get('annee',None))
            
            gboite = request.POST.get('boite',None)
            gnb_seats = int(request.POST.get('nb_seats',None))
            gnb_bags = int(request.POST.get('nb_bags',None))
            gnb_ports = int(request.POST.get('nb_ports',None))
            
            gcolor = request.POST.get('color',None)
            
            getat = request.POST.get('etat',None)
            gdescription = request.POST.get('description',None)
            
            gcaution= float(request.POST.get('caution',None))
            gprix_jour = float(request.POST.get('prix_jour',None))
            
            gphoto = request.FILES.get('photo',None)

            gid_marquer = request.POST.get('id_marquer',None)
            m=Marquer.objects.filter(id=gid_marquer).first()
            

            v01=Voiture.objects.filter(numero_series=gnumero_series).first()
            if(v01!=None):
                if(gphoto!=None):
                    Voiture.objects.filter(numero_series=gid).update(
                        numero_series=gnumero_series,
                        modele=gmodele,
                        class_voiture=gclass_voiture,
                        annee=gannee,

                        boite=gboite,
                        nb_seats=gnb_seats,
                        nb_bags=gnb_bags,
                        nb_ports=gnb_ports,

                        color=gcolor,

                        etat=getat,
                        description=gdescription,

                        caution=gcaution,
                        prix_jour=gprix_jour,

                        id_marquer=m
                    )
                    if(v01.photo!="default_image.jpg"):
                        v01.photo.delete()
                    v01.photo=gphoto
                    v01.save()
                else:
                    Voiture.objects.filter(numero_series=gid).update(
                        numero_series=gnumero_series,
                        modele=gmodele,
                        class_voiture=gclass_voiture,
                        annee=int(gannee),

                        boite=gboite,
                        nb_seats=gnb_seats,
                        nb_bags=gnb_bags,
                        nb_ports=gnb_ports,

                        color=gcolor,

                        etat=getat,
                        description=gdescription,

                        caution=gcaution,
                        prix_jour=gprix_jour,

                        id_marquer=m
                    )
                
                
                return Response({'Response': 'Success'})
            return Response({'Response': 'Not Exist'})   
        except:
            return Response({'Response': 'Failed'})




#Api for Transfer Pages
class GetAllTransfer(APIView):
    def post(self, request):
        try:
            t=Transfer.objects.all()
            if(t!=None):
                serialized_obj = serializers.serialize('json',t)
                return Response({'Response': 'Success',"Transfers":serialized_obj})
            return Response({'Response': 'Not Exist'})
        except:
            return Response({'Response': 'Failed'})

class SearchTransfer(APIView):
    def post(self, request):

        try:
            gsearchValue = request.POST.get('searchValue', None)
            gdate_Start = request.POST.get('date_Start', None)#yyyy-MM-dd kk:mm __range
            gdate_End = request.POST.get('date_End', None)#yyyy-MM-dd kk:mm
            search01=Transfer.objects.all()
            searchStatue=False
        
            #search by rang date

            if(gdate_Start!="" and gdate_End!=""):
                date_Start=datetime.strptime(gdate_Start, "%Y-%m-%d %H:%M:%S")
                date_End=datetime.strptime(gdate_End, "%Y-%m-%d %H:%M:%S")
                search02=Transfer.objects.filter(date_depar__range=(date_Start,date_End)).all()
                if (len(search02)!=0):
                    search01=search02
                    searchStatue=True
                
                    #search by searchValue

                    if(gsearchValue!=""):
                        c=Client.objects.filter(nomprenom__contains=gsearchValue).all()
                        if(len(c)!=0):
                            d=Demande.objects.select_related('id_client').filter(id_client__in=c).all()
                            if(len(d)!=0):
                                search03=Transfer.objects.select_related('id_demande').filter(id_demande__in=d)
                                if(len(search03)!=0):
                                    search01=search01 & search03
                                    searchStatue=True
                                    

                        #Inner Join with Voiture
                        
                        v01 = Voiture.objects.filter(
                            Q(annee__contains=gsearchValue) |
                            Q(class_voiture__contains=gsearchValue) |
                            Q(modele__contains=gsearchValue)).all()
                        
                        m=Marquer.objects.filter(nom__contains=gsearchValue).all()
                        v02=[]
                        if(len(m)!=0):
                            v02=Voiture.objects.select_related('id_marquer').filter(id_marquer__in=m).all()
                        
                        
                        if(len(v01)!=0):
                            if(len(v02)!=0):
                                v03=v01 & v02
                            else:
                                v03=v01
                        else:
                            v03=v02
                        search04=Transfer.objects.select_related('numero_series').filter(numero_series__in=v03).all()
                        if(len(search04)!=0):
                            search01=search01 & search04
                            searchStatue=True
                            
                    
        
            if(searchStatue):
                serialized_obj = serializers.serialize('json',search01)
                return Response({'Response': 'Success',"Transfers":serialized_obj})
            return Response({'Response': 'Not Exist'})
        except:
            return Response({'Response': 'Failed'})

class Update_Etat_Transfer(APIView):
    def post(self, request):
        
        try:
            gidTransfer = request.POST['idTransfer']
            getat = request.POST['etat']
            gprix = request.POST['prix']
 

            t=Transfer.objects.filter(id=gidTransfer).first()
            if(t!=None):
                t.id_demande.etat=getat
                t.id_demande.save()
                if(getat=="Annuler"):
                    Annulation.objects.create(date=datetime.now(),description='Admin annuler Cette Demande',id_demande=t.id_demande.id)
                if(getat=="En Cours"):
                    Paiment.objects.create(prix=gprix,date=datetime.now(),type='Cash',id_client=t.id_demande.id_client,id_demande=t.id_demande)
            
                return Response({'Response': 'Success'})
            return Response({'Response': 'Not Exist'})
        except:
            return Response({'Response': 'Failed'})

class GetAllListTransfer(APIView):
    def post(self, request):
        try:
            lt=ListTransfer.objects.all()
            if(lt!=None):
                serialized_obj = serializers.serialize('json',lt)
                return Response({'Response': 'Success',"ListTransfers":serialized_obj})
            return Response({'Response': 'Not Exist'})
        except:
            return Response({'Response': 'Failed'})

class Insert_Update_ListTransfer(APIView):
    def post(self, request):
        try:
            gid = int(request.POST.get('id',None))
            gaddress_depart = request.POST.get('address_depart',None)
            gaddress_fin = request.POST.get('address_fin',None)
            gprix = float(request.POST.get('prix',None))
            if(gid==0):
                if(ListTransfer.objects.filter(address_depart=gaddress_depart,address_fin=gaddress_fin).first()==None):
                    lt=ListTransfer.objects.create(address_depart=gaddress_depart,address_fin=gaddress_fin,prix=gprix)
                    serialized_obj = serializers.serialize('json',[lt,])
                    return Response({'Response': 'Success',"ListTransfer":serialized_obj})
                return Response({'Response': 'Exist'})
            else:
                lt=ListTransfer.objects.filter(id=gid).first()
                if (lt!=None):
                    ListTransfer.objects.filter(id=gid).update(address_depart=gaddress_depart,address_fin=gaddress_fin,prix=gprix)
                    lt=ListTransfer.objects.filter(id=gid).first()
                    serialized_obj = serializers.serialize('json',[lt,])
                    return Response({'Response': 'Success',"ListTransfer":serialized_obj})
                return Response({'Response': 'Not Exist'})

        except:
            return Response({'Response': 'Failed'})
 
#Api for Exurcion Pages
class GetAllExurcion(APIView):
    def post(self, request):
        try:
            e=Exurcion.objects.all()
            if(e!=None):
                serialized_obj = serializers.serialize('json',e)
                return Response({'Response': 'Success',"Exurcions":serialized_obj})
            return Response({'Response': 'Not Exist'})
        except:
            return Response({'Response': 'Failed'})

class SearchExurcion(APIView):
    def post(self, request):

        try:
            gsearchValue = request.POST.get('searchValue', None)
            gdate_Start = request.POST.get('date_Start', None)#yyyy-MM-dd kk:mm __range
            gdate_End = request.POST.get('date_End', None)#yyyy-MM-dd kk:mm
            search01=Exurcion.objects.all()
            searchStatue=False
        
            #search by rang date

            if(gdate_Start!="" and gdate_End!=""):
                date_Start=datetime.strptime(gdate_Start, "%Y-%m-%d %H:%M:%S")
                date_End=datetime.strptime(gdate_End, "%Y-%m-%d %H:%M:%S")
                search02=Exurcion.objects.filter(date_depar__range=(date_Start,date_End)).all()
                if (len(search02)!=0):
                    search01=search02
                    searchStatue=True
                
                    #search by searchValue

                    if(gsearchValue!=""):
                        c=Client.objects.filter(nomprenom__contains=gsearchValue).all()
                        if(len(c)!=0):
                            d=Demande.objects.select_related('id_client').filter(id_client__in=c).all()
                            if(len(d)!=0):
                                search03=Exurcion.objects.select_related('id_demande').filter(id_demande__in=d)
                                if(len(search03)!=0):
                                    search01=search01 & search03
                                    searchStatue=True
                                    

                        #Inner Join with Voiture
                        
                        v01 = Voiture.objects.filter(
                            Q(annee__contains=gsearchValue) |
                            Q(class_voiture__contains=gsearchValue) |
                            Q(modele__contains=gsearchValue)).all()
                        
                        m=Marquer.objects.filter(nom__contains=gsearchValue).all()
                        v02=[]
                        if(len(m)!=0):
                            v02=Voiture.objects.select_related('id_marquer').filter(id_marquer__in=m).all()
                        
                        
                        if(len(v01)!=0):
                            if(len(v02)!=0):
                                v03=v01 & v02
                            else:
                                v03=v01
                        else:
                            v03=v02
                        search04=Exurcion.objects.select_related('numero_series').filter(numero_series__in=v03).all()
                        if(len(search04)!=0):
                            search01=search01 & search04
                            searchStatue=True
                            
                    
        
            if(searchStatue):
                serialized_obj = serializers.serialize('json',search01)
                return Response({'Response': 'Success',"Exurcions":serialized_obj})
            return Response({'Response': 'Not Exist'})
        except:
            return Response({'Response': 'Failed'})

class Update_Etat_Exurcion(APIView):
    def post(self, request):
        
        try:
            gidExurcion = request.POST['idExurcion']
            getat = request.POST['etat']
            gprix = request.POST['prix']

            e=Exurcion.objects.filter(id=gidExurcion).first()
            if(e!=None):
                e.id_demande.etat=getat
                e.id_demande.save()
                if(getat=="Annuler"):
                    Annulation.objects.create(date=datetime.now(),description='Admin annuler Cette Demande',id_demande=e.id_demande.id)
                if(getat=="En Cours"):
                    Paiment.objects.create(prix=gprix,date=datetime.now(),type='Cash',id_client=e.id_demande.id_client,id_demande=e.id_demande)
            
                return Response({'Response': 'Success'})
            return Response({'Response': 'Not Exist'})
        except:
            return Response({'Response': 'Failed'})

class GetAllListExurcion(APIView):
    def post(self, request):
        try:
            le=ListExurcion.objects.all()
            if(le!=None):
                serialized_obj = serializers.serialize('json',le)
                return Response({'Response': 'Success',"ListExurcions":serialized_obj})
            return Response({'Response': 'Not Exist'})
        except:
            return Response({'Response': 'Failed'})

class Insert_Update_ListExurcion(APIView):
    def post(self, request):
        try:
            gid = int(request.POST.get('id',None))
            gaddress_depart = request.POST.get('address_depart',None)
            gdescription = request.POST.get('description',None)
            gprix = float(request.POST.get('prix',None))
            if(gid==0):
                if(ListExurcion.objects.filter(address_depart=gaddress_depart).first()==None):
                    le=ListExurcion.objects.create(address_depart=gaddress_depart,description=gdescription,prix=gprix)
                    serialized_obj = serializers.serialize('json',[le,])
                    return Response({'Response': 'Success',"ListExurcion":serialized_obj})
                return Response({'Response': 'Exist'})
            else:
                le=ListExurcion.objects.filter(id=gid).first()
                if (le!=None):
                    ListExurcion.objects.filter(id=gid).update(address_depart=gaddress_depart,description=gdescription,prix=gprix)
                    le=ListExurcion.objects.filter(id=gid).first()
                    serialized_obj = serializers.serialize('json',[le,])
                    return Response({'Response': 'Success',"ListExurcion":serialized_obj})
                return Response({'Response': 'Not Exist'})
        except:
            return Response({'Response': 'Failed'})

#Api for Post Pages
class GetAllPost(APIView):
    def post(self, request):
        try:
            p=Post.objects.all()
            if(p!=None):
                serialized_obj = serializers.serialize('json',p)
                return Response({'Response': 'Success',"Posts":serialized_obj})
            return Response({'Response': 'Not Exist'})
        except:
            return Response({'Response': 'Failed'})
        
class InserPost(APIView):
    def post(self, request):
            
        try:
            gtitle = request.POST.get('title',None)
            gdescriptions = request.POST.get('descriptions',None)
            gdate_depart = request.POST.get('date_depart',None)
            gdate_fin = request.POST.get('date_fin',None)
            glien = request.POST.get('lien',None)
            
            gdate_depart=datetime.strptime(gdate_depart, "%Y-%m-%d %H:%M:%S")
            gdate_fin=datetime.strptime(gdate_fin, "%Y-%m-%d %H:%M:%S")
            
            gphoto = request.FILES.get('photo',None)

            if(gphoto!=None):
                p=Post.objects.create(
                    title=gtitle,
                    descriptions=gdescriptions,
                    date_depart=gdate_depart,
                    date_fin=gdate_fin,
                    lien=glien,
                )
                p.photo.delete()
                p.photo=gphoto
                p.save()
            else:
                p=Post.objects.create(
                    title=gtitle,
                    descriptions=gdescriptions,
                    date_depart=gdate_depart,
                    date_fin=gdate_fin,
                    lien=glien,
                )
            sendNotificationForClient(gtitle,gdescriptions,dataObject=None)
            serialized_obj = serializers.serialize('json',[p,])
            return Response({'Response': 'Success',"Post":serialized_obj})
        
            
        except:
            return Response({'Response': 'Failed'})

class UpdatePost(APIView):
    def post(self, request):

        try:  
            gid = request.POST.get('id',None)
            gtitle = request.POST.get('title',None)
            gdescriptions = request.POST.get('descriptions',None)
            gdate_depart = request.POST.get('date_depart',None)
            gdate_fin = request.POST.get('date_fin',None)
            glien = request.POST.get('lien',None)
            gdate_depart=datetime.strptime(gdate_depart, "%Y-%m-%d %H:%M:%S")
            gdate_fin=datetime.strptime(gdate_fin, "%Y-%m-%d %H:%M:%S")
            
            gphoto = request.FILES.get('photo',None)

            if(gphoto!=None):
                Post.objects.filter(id=gid).update(
                    title=gtitle,
                    descriptions=gdescriptions,
                    date_depart=gdate_depart,
                    date_fin=gdate_fin,
                    lien=glien,
                )
                p=Post.objects.filter(id=gid).first()
                if(p.photo!="default_image.jpg"):
                    p.photo.delete()
                p.photo=gphoto
                p.save()
            else:
                Post.objects.filter(id=gid).update(
                    title=gtitle,
                    descriptions=gdescriptions,
                    date_depart=gdate_depart,
                    date_fin=gdate_fin,
                    lien=glien,
                )
            p=Post.objects.filter(id=gid).first()
            sendNotificationForClient(gtitle,gdescriptions,dataObject=None)
            serialized_obj = serializers.serialize('json',[p,])
            return Response({'Response': 'Success',"Post":serialized_obj})        
        except:
            return Response({'Response': 'Failed'})

#Api for Paiment Pages
class GetAllPaiment(APIView):
    def post(self, request):
        try:
            p=Paiment.objects.all()
            if(p!=None):
                serialized_obj = serializers.serialize('json',p)
                return Response({'Response': 'Success',"Paiments":serialized_obj})
            return Response({'Response': 'Not Exist'})
        except:
            return Response({'Response': 'Failed'})
      
#Api for Paiment Pages
class GetAllAnnulation(APIView):
    def post(self, request):
        try:
            a=Annulation.objects.all()
            if(a!=None):
                serialized_obj = serializers.serialize('json',a)
                return Response({'Response': 'Success',"Annulations":serialized_obj})
            return Response({'Response': 'Not Exist'})
        except:
            return Response({'Response': 'Failed'})
      
class SendNotification(APIView):
    def post(self, request):
        title="Title 01"
        body="Body"
        s=''
        
        s=sendNotificationForAdmin(title=title,body=body)
        #s=sendNotificationForClient(title=title,body=body)

        return Response({"send":s})