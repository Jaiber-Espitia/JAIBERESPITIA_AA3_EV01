from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from contacts.models import CustomersManagement
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.contrib.auth.decorators import login_required


# Vista para gestionar los contactos y crear campañas de marketing.
@login_required(redirect_field_name="login")
def contact_management(request):
    customers = CustomersManagement.objects.all()
    context = {
        "customers": customers
    }
    return render(request, "contacts.html", context=context)



# Vista para agregar un nuevo cliente
@login_required(redirect_field_name="login")
def add_contact(request):
    if request.method == "POST":
        customer = CustomersManagement.objects.create(
            customer=request.POST.get("customer"),
            address=request.POST.get("address"),
            position=request.POST.get("position"),
            interaction=request.POST.get("interaction"),
            preference=request.POST.get("preference"),
            notes=request.POST.get("notes"),
            campaing=request.POST.get("campaing"),
            email=request.POST.get("email"),
            phone_number=request.POST.get("phoneNumber"),
            status=request.POST.get("status")
        )

        customer.save()
        messages.success(request, "Cliente agregado con exito!")

    return redirect("contacts")


# Vista para actulizar un cliente
@login_required(redirect_field_name="login")
def update_customer(request, pk:None):
    if request.method == "POST":
        customer = CustomersManagement.objects.get(id=pk)
        customer_info = {
            "customer": request.POST.get("customer"),
            "interaction": request.POST.get("interaction"),
            "address": request.POST.get("address"),
            "position": request.POST.get("position"),
            "preference": request.POST.get("preference"),
            "notes": request.POST.get("notes"),
            "campaing": request.POST.get("campaing"),
            "email": request.POST.get("email"),
            "phoneNumber": request.POST.get("phoneNumber"),
            "status": request.POST.get("status"),
        }
        customer.customer = customer_info.get("customer")
        customer.interaction = customer_info.get("interaction")
        customer.address = customer_info.get("address")
        customer.position = customer_info.get("position")
        customer.preference = customer_info.get("preference")
        customer.notes = customer_info.get("notes")
        customer.campaing = customer_info.get("campaing")
        customer.email = customer_info.get("email")
        customer.phone_number = customer_info.get("phoneNumber")
        customer.status = customer_info.get("status")

        customer.save()
        messages.success(request, "Cliente actualizado con exito!")

    return redirect("contacts")

# Vista para eliminar un cliente
@login_required(redirect_field_name="login")
def delete_customer(request, pk):
    if request.method == "POST":
        customer = CustomersManagement.objects.get(id=pk)
        customer.delete()
    return redirect("contacts")   


# Vista para crear una campaña de marketing a un cliente
@login_required(redirect_field_name="login")
def send_marketing_campaing(request, pk: None):
  
    if request.method == "POST":
        customer = CustomersManagement.objects.get(id=pk)
        html_message = ""
        if request.POST.get("selectNewCampaing") == "Black_friday":
            html_message = render_to_string("black_friday_marketing.html")

        elif request.POST.get("selectNewCampaing") == "Servicios_digitales":
            html_message = render_to_string("digital_platform_marketing.html")

        elif request.POST.get("selectNewCampaing") == "Redes_sociales":
            html_message = render_to_string("social_media_marketing.html")

        elif request.POST.get("selectNewCampaing") == "Temporada_navideña":
            html_message = render_to_string("christmas_season_marketing.html")
        
        elif request.POST.get("selectNewCampaing") == "Nuevo_cliente":
            html_message = render_to_string("welcome.html", context={"customer": customer})

            
        subject = request.POST.get("emailSubject")
        recipient = [request.POST.get("emailUser")]


        email_from = settings.EMAIL_HOST_USER
        plain_message = strip_tags(html_message)

        message = EmailMultiAlternatives(
                    subject,
                    plain_message,
                    email_from,
                    recipient
                )

        message.attach_alternative(html_message, "text/html")
        message.send()
        customer.campaing = "Campaña agregada"
        customer.save()
        messages.success(request, "Campañada creada con exito!")

    return redirect("contacts")
