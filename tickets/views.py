from django.shortcuts import render, redirect
from tickets.models import Tickets
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from contacts.models import CustomersManagement


# Vista para la gestion de tickets
@login_required(redirect_field_name="login")
def tickets_management(request):
    tickets = Tickets.objects.all()

    # Total de tickets
    all_tickets_created = Tickets.objects.count()

    # Tickets abiertos
    open_tickets = Tickets.objects.filter(status="Abierto").count() 

    # Tickets abiertos
    closed_tickets = Tickets.objects.filter(status="Cerrado").count() 

    context = {
        "tickets": tickets,
        "all_tickets_created": all_tickets_created,
        "open_tickets": open_tickets,
        "closed_tickets": closed_tickets
    }

    return render(request, "tickets.html", context=context)


# Vista para generar un nuevo ticket
@login_required(redirect_field_name="login")
def generate_ticket_form(request):
    all_customers = CustomersManagement.objects.all()
    tickets = Tickets.objects.all()
    if request.method == "POST":
        get_customer_id = CustomersManagement.objects.get(customer=request.POST.get("customer"))
        new_ticket = Tickets.objects.create(
            subject=request.POST.get("subject"),
            customer=get_customer_id,
            asigned_to=request.POST.get("asigned"),
            agent=request.POST.get("agent"),
            description=request.POST.get("description"),
            priority=request.POST.get("priority"),
            status=request.POST.get("status"),
            ticket_type=request.POST.get("ticketType"),
            chanel=request.POST.get("channel")
        )
        new_ticket.save()
        messages.success(request, "¡Ticket creado con exito!")

    context = {
        "tickets": tickets,
        "customers":all_customers
    }
    return render(request, "generate_ticket_form.html", context=context)


# Vista para cerrar un ticket
@login_required(redirect_field_name="login")
def close_ticket(request, pk: None):
    ticket = Tickets.objects.get(id=pk)
    if request.method == "POST":
        ticket.status = "Cerrado"
        ticket.save()
    return redirect("tickets")


# vista para eliminar ticket
@login_required(redirect_field_name="login")
def delete_ticket(request, pk):
    ticket = Tickets.objects.get(id=pk)
    if request.method == "POST":
        ticket.delete()
    return redirect("tickets")