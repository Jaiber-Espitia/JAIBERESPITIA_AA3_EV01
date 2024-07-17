from django.urls import path
from django.conf import settings
from . import views
from django.conf.urls.static import static


urlpatterns = [
    path('contacts/', view=views.contact_management, name="contacts"),
    path('addContact/', view=views.add_contact, name="add_contact"),
    path('deleteContact/<str:pk>', view=views.delete_customer, name="delete_contact"),
    path('updateContact/<str:pk>', view=views.update_customer, name="update_contact"),
    path('marketingCampaing/<str:pk>', view=views.send_marketing_campaing, name="marketing_campaing"),
    

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)