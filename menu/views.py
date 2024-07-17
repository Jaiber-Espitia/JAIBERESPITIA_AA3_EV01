from django.shortcuts import render
from django.contrib.auth.models import User
from tasks.models import TasksManagement, AssignTask
from contacts.models import CustomersManagement
from tickets.models import Tickets
from inventory.models import (
    Product,
    Order,
    Brand,
    Category,
    Store
)


# Vista del panel de graficos estadisticos
def dashboard(request):

    # Estadisticas de la gestion de area
    tasks = TasksManagement.objects.filter(status="en proceso").count()
    tasks_done = TasksManagement.objects.filter(status="Finalizada").count()

    # Estadisticas del control de inventario
    orders = Order.objects.count()
    products = Product.objects.count()
    brands = Brand.objects.count()
    categories = Category.objects.count()
    stores = Store.objects.count()

    # Estadisticas del control de los tickets
    all_tickets = Tickets.objects.count()
    closed_tickets= Tickets.objects.filter(status="Cerrado").count()
    open_tickets= Tickets.objects.filter(status="Abierto").count()

    # Estadisticas de la gestion de contactos y campañas de marketing
    customers = CustomersManagement.objects.count()
    active_customers = CustomersManagement.objects.filter(status="Activo").count()
    customers_marketing_campaings = CustomersManagement.objects.filter(campaing="Campaña agregada").count()
    no_marketing_campaings = CustomersManagement.objects.filter(campaing="Sin campaña").count()

    # Tareas asignadas
    assigned_tasks = AssignTask.objects.all().count()

    # usuarios registrados
    users = User.objects.all().count()
    
    context = {
        "tasks": tasks,
        "is_finished": tasks_done,
        "customers": customers,
        "active_customers": active_customers,
        "customers_campaing": customers_marketing_campaings,
        "no_marketing_campaing": no_marketing_campaings,
        "orders": orders,
        "products": products,
        "brands": brands,
        "categories": categories,
        "stores": stores,
        "tickets": all_tickets,
        "closed_tickets": closed_tickets,
        "open_tickets": open_tickets,
        "assigned_tasks": assigned_tasks,
        "users": users,
    }
    return render(request, "dashboard.html", context=context)
