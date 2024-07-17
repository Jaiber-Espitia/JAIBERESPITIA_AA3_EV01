from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path('', include("authentication.urls")),
    path('', include("menu.urls")),
    path('', include("tasks.urls")),
    path('', include("contacts.urls")),
    path('', include("tickets.urls")),
    path('', include("inventory.urls")),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

