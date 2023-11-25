from django.contrib import admin
from polls.models import Admin , Client , Demande , Voiture ,Gallery, Reservation ,  Transfer , Exurcion , Paiment , Options ,Marquer , Service ,Annulation , Post , ListExurcion , ListTransfer 
admin.site.register(Client)
admin.site.register(Admin)
admin.site.register(Demande)
admin.site.register(Voiture)
admin.site.register(Reservation)
admin.site.register(Transfer)
admin.site.register(Exurcion)
admin.site.register(Gallery)
admin.site.register(ListTransfer)
admin.site.register(ListExurcion)
admin.site.register(Paiment)
admin.site.register(Options)
admin.site.register(Marquer)
admin.site.register(Service)
admin.site.register(Annulation)
admin.site.register(Post)
# Register your models here.
