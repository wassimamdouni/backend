from rest_framework import serializers
from polls.models import Admin ,  Client , Demande , Voiture , Transfer , Reservation , Marquer , Options , Paiment , Service , Post , ListTransfer , ListExurcion , Gallery

class AdminsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class MarquerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marquer
        fields = '__all__'

class VoitureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voiture
        fields = '__all__'

class DemandeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Demande
        fields = '__all__'

class OptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Options
        fields = '__all__'

class PaimentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paiment
        fields = '__all__'

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'

class TransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transfer
        fields = '__all__'
class ListTransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListTransfer
        fields = '__all__'

class ListExurcionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListExurcion
        fields = '__all__'

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model= Post
        fields = '__all__'
class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields= '__all__'
class VoituresSerializer(serializers.Serializer):
    numero_series = serializers.CharField()
    modele = serializers.CharField()
    nb_seats = serializers.CharField()
    nb_bags = serializers.CharField()
    nb_ports = serializers.CharField()
    prix_jour = serializers.FloatField()
    caution= serializers.FloatField()
    annee = serializers.CharField()
    etat = serializers.CharField()
    boite= serializers.CharField()
    marque = serializers.CharField()
    photoMarque = serializers.ImageField()
    photo = serializers.ImageField()  # Assuming it's a string field
    description = serializers.CharField()
    class_voiture = serializers.CharField()
    id_marquer = serializers.CharField()
    disponibilite = serializers.CharField()