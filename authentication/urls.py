from django.urls import path
from django.conf import settings
from . import views
from django.conf.urls.static import static


urlpatterns = [
    path('', view=views.home_page, name="home"),
    path('login/', view=views.user_login, name="login"),
    path('register/', view=views.user_registration, name="register"),
    path('change_password/', view=views.restart_password, name="change_password"),
    path('logout/', view=views.user_logout, name="logout"),
    path('about/', view=views.about_us, name="about"),
    path('contact/', view=views.contact_us, name="contact_us"),
    

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)