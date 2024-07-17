from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from smtplib import SMTPException
from authentication.forms import CreateNewUser, ChangePasswordForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash #keep it the user session active
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings


# Vista del Home Page
def home_page(request):
    return render(request, "base.html")


# Vista de registro de usuario, Valida los datos del formulario.
def user_registration(request):

    form = CreateNewUser()

    if request.method == "POST":
        form = CreateNewUser(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            form.save()
            messages.success(request, f"Usuario '{username}' registrado con exito!")

        elif request.POST["password1"] != request.POST["password2"]:
            messages.error(request, "Error, las contraseñas ingresadas no coinciden.")

        elif User.objects.filter(username=request.POST["username"]).exists():
            messages.error(request, "Error, el usuario ya se encuentra registrado.")

        elif User.objects.filter(email=request.POST["email"]).exists():
            messages.error(request, "Error, el email ingresado ya se encuentra en uso.")

    context = {
        "form": form
    }

    return render(request, "register.html", context=context)


# Vista de login de usuario
def user_login(request):

    form = CreateNewUser()

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("dashboard")
        else:
            messages.error(request,"Error, usuario o contraseña incorrecta!")

    context = {
        "form": form
    }

    return render(request, "login.html", context=context)


# Vista de reestablecer contraseña
@login_required(redirect_field_name="login")
def restart_password(request):
    form = ChangePasswordForm(request.user)
    if request.method == "POST":
        form = ChangePasswordForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "¡Contraseña actualizada con exito! inicie sesión de nuevo.")
        else:
            messages.error(request, "Error, ¡las contraseñas no coinciden!")
    
    context = {
        "form": form
    }

    return render(request, "change_password.html", context=context)


# Vista para cerrar la sesion
def user_logout(request):
    logout(request)
    return redirect("home")


# Vista sobre informacion de la App
def about_us(request):
    return render(request, "about_us.html")


# Vista para acceder al formulario de contacto
def contact_us(request):
    try:
        if request.method == "POST":
            subject = request.POST.get("subject")
            body_message = request.POST.get("message")
            from_email = settings.EMAIL_HOST_USER
            send_message_to = [request.POST.get("email")]
    
            message = EmailMultiAlternatives(
                subject,
                body_message,
                from_email,
                send_message_to
            )
            
            message.send()
            messages.success(request, "Mensaje enviado con exito!")

    except SMTPException as e:
        messages.error(request, "Ocurrio un error al enviar el mensaje!", e)

    return render(request, "contact_us.html")