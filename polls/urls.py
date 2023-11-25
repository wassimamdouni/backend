from django.urls import path , include

from . import views

urlpatterns = [
    path('InserClient', views.InserClient.as_view()),
    path('SendNotificationClient', views.SendNotificationClient.as_view()),
    path('InserClientTranfer', views.InserClientTranfer.as_view()),
    path('Insert_reservation', views.Insert_reservation.as_view()),
    path('Insert_transfer', views.Insert_transfer.as_view()),
    path('Insert_exurcion', views.Insert_exurcion.as_view()),
    path('InserAnnulation', views.InserAnnulation.as_view()),
    path('InsertPiaemnt', views.InsertPiaemnt.as_view()),
    path('Effect_paiment', views.Effect_paiment.as_view()),
    path('Verification', views.Verification.as_view()),
    path('AfficherListTransfer', views.AfficherListTransfer.as_view()),
    path('AfficherListExurcion', views.AfficherListExurcion.as_view()),
     path('AfficherListTransfer1', views.AfficherListTransfer.as_view()),
    path('AfficherListExurcion1', views.AfficherListExurcion.as_view()),
    path('Afficher_Gallery', views.Afficher_Gallery.as_view()),
    path('Afficher_Client', views.Afficher_Client.as_view()),
    path('Afficher_Voitures', views.Afficher_Voitures.as_view()),
    path('Afficher_Voitures1', views.Afficher_Voitures1.as_view()),
    path('getNumeroSeries', views.getNumeroSeries.as_view()),
    path('Afficher_demande_Client', views.Afficher_demande_Client.as_view()),
    path('Afficher_OptionVoitures', views.Afficher_OptionVoitures.as_view()),
    path('Afficher_Post', views.Afficher_Post.as_view()),
    path('UpadateClientPassword',views.UpadateClientPassword.as_view()),
    path('UpdateClient', views.UpdateClient.as_view()),
    path('ContinueInscriClient', views.ContinueInscriClient.as_view()),

    #--------------------------------------------------------------------
    #--------------------------------------------------------------------
    
    #Login Admin
    path('Login_Admin', views.Login_Admin.as_view()),
    path('Validation_Login', views.Validation_Login.as_view()),
    path('Resend_Code_Login', views.Resend_Code_Login.as_view()),
    path('Test_Login_Admin', views.Test_Login_Admin.as_view()),
    path('Update_Admin', views.Update_Admin.as_view()),

    #Forget Password Admin
    path('Forget_Password_Admin', views.Forget_Password_Admin.as_view()),
    path('Validation_Forget_Password', views.Validation_Forget_Password.as_view()),
    path('Resend_Code_Forget_Password', views.Resend_Code_Forget_Password.as_view()),
    path('New_Password_Admin', views.New_Password_Admin.as_view()),

    #Get Models
    path('GetClient', views.GetClient.as_view()),
    path('GetAdmin', views.GetAdmin.as_view()),
    path('GetVoiture', views.GetVoiture.as_view()),
    path('GetMarquer', views.GetMarquer.as_view()),
    path('GetDemande', views.GetDemande.as_view()),
    path('GetReservation', views.GetReservation.as_view()),
    path('GetService', views.GetService.as_view()),
    path('GetListTransfer', views.GetListTransfer.as_view()),
    path('GetListExurcion', views.GetListExurcion.as_view()),


    #Reservation Api
    path('GetAllReservation', views.GetAllReservation.as_view()),
    path('SearchReservation', views.SearchReservation.as_view()),
    path('Update_Etat_Demande', views.Update_Etat_Demande.as_view()),

    #Client Api
    path('GetAllClient', views.GetAllClient.as_view()),
    path('SearchClient', views.SearchClient.as_view()),
    path('ActivateClient', views.ActivateClient.as_view()),

    #Voiture Api
    path('GetAllMarquer', views.GetAllMarquer.as_view()),
    path('GetAllVoiture', views.GetAllVoiture.as_view()),
    path('Insert_Update_Marquer', views.Insert_Update_Marquer.as_view()),
    path('SearchVoiture', views.SearchVoiture.as_view()),
    path('GetOptions', views.GetOptions.as_view()),
    path('InserVoiture', views.InserVoiture.as_view()),
    path('InserOption', views.InserOption.as_view()),
    path('DeleteOption', views.DeleteOption.as_view()),
    path('UpdateVoiture', views.UpdateVoiture.as_view()),

    #Transfer Api
    path('GetAllTransfer', views.GetAllTransfer.as_view()),
    path('SearchTransfer', views.SearchTransfer.as_view()),
    path('Update_Etat_Transfer', views.Update_Etat_Transfer.as_view()),
    path('GetAllListTransfer', views.GetAllListTransfer.as_view()),
    path('Insert_Update_ListTransfer', views.Insert_Update_ListTransfer.as_view()),
    
    #Exurcion' Api
    path('GetAllExurcion', views.GetAllExurcion.as_view()),
    path('SearchExurcion', views.SearchExurcion.as_view()),
    path('Update_Etat_Exurcion', views.Update_Etat_Exurcion.as_view()),
    path('GetAllListExurcion', views.GetAllListExurcion.as_view()),
    path('Insert_Update_ListExurcion', views.Insert_Update_ListExurcion.as_view()),
    path('GetGallery', views.GetGallery.as_view()),
    path('InserGallery', views.InserGallery.as_view()),
    path('DeleteGallery', views.DeleteGallery.as_view()),

    #Post Api
    path('GetAllPost', views.GetAllPost.as_view()),
    path('InserPost', views.InserPost.as_view()),
    path('UpdatePost', views.UpdatePost.as_view()),

    #Api for Paiment Pages
    path('GetAllPaiment', views.GetAllPaiment.as_view()),

    #Api for Annulation Pages
    path('GetAllAnnulation', views.GetAllAnnulation.as_view()),


    path('SendNotification', views.SendNotification.as_view()),





]