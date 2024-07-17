from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from tasks.models import (
    TasksManagement,
    AssignTask,
    TeamMember,
    Department
)


# Vista principal de Tareas
@login_required(redirect_field_name="login")
def task_manager(request):
    
    tasks = TasksManagement.objects.all()

    context = {
        "tasks": tasks
    }
    return render(request, "tasks.html", context=context)


# Vista para eliminar tarea de la base de datos por medio de su ID.
@login_required(redirect_field_name="login")
def delete_task(request, pk): 
    if request.method == "POST":  
        tasks = TasksManagement.objects.get(id=pk)
        tasks.delete()
    return redirect("tasks")


# Vista para agregar una tarea nueva.
@login_required(redirect_field_name="login")
def add_task(request):
    user_data = {
        "name": request.POST.get("taskName"),
        "description": request.POST.get("taskDescription"),
        "priority": request.POST.get("taskPriority"),
        "status": request.POST.get("taskStatus"),
        "due_date": request.POST.get("dueDate")
    }
    if request.method == "POST":
        tasks = TasksManagement.objects.create(
            title=user_data.get("name"),
            description=user_data.get("description"),
            priority=user_data.get("priority"),
            status=user_data.get("status"),
            due_date=user_data.get("due_date"),
        )

        tasks.save()
        messages.success(request, "Tarea agregada con exito!")
    return redirect("tasks")


#Vista para actualizar una tarea
@login_required(redirect_field_name="login")
def update_task(request, pk: None):
    if request.method == "POST":
        tasks = TasksManagement.objects.get(id=pk)
        user_data = {
            "title": request.POST.get("taskName"),
            "description": request.POST.get("taskDescription"),
            "priority": request.POST.get("taskPriority"),
            "status": request.POST.get("taskStatus"),
            "due_date": request.POST.get("dueDate"),
        }
        tasks.title = user_data.get("title")
        tasks.description = user_data.get("description")
        tasks.priority = user_data.get("priority")
        tasks.status = user_data.get("status")
        tasks.due_date = user_data.get("due_date")
        tasks.save()

        messages.success(request, "Tarea acualizada con exito!")
    
    return redirect("tasks")



# Vista para finalizar una tarea
@login_required(redirect_field_name="login")
def task_is_finished(request, pk: None):
    if request.method == "POST":
        tasks = TasksManagement.objects.get(id=pk)
        tasks.status = "Finalizada"
        tasks.save()

    return redirect("tasks")


# -------------------------------  Asignacion de tasks ---------------------------------------


# Vista para la asignacion de tasks
@login_required(redirect_field_name="login")
def assign_task(request):
    departments = Department.objects.all()
    team_members = TeamMember.objects.all()
    assigned_tasks = AssignTask.objects.all()

    context = {
        "assignedTasks": assigned_tasks,
        "teamMembers": team_members,
        "departments": departments
    }

    return render(request, "assign_task.html", context=context)


# Vista para asignar una tarea nueva
@login_required(redirect_field_name="login")
def assign_new_task(request):
    if request.method == "POST":
        team_member = TeamMember.objects.get(name=request.POST.get("assignedTo"))
        department = Department.objects.get(name=request.POST.get("department"))

        assign_task = AssignTask.objects.create(
            title=request.POST.get("taskName"),
            description=request.POST.get("taskDescription"),
            status=request.POST.get("taskStatus"),
            priority=request.POST.get("taskPriority"),
            due_date=request.POST.get("dueDate"),
            team_member=team_member,
            department=department
        )
        assign_task.save()

        messages.success(request, "Tarea asignada con exito!")

    return redirect("assign_task")
    

# Vista para asignar una tarea nueva
@login_required(redirect_field_name="login")
def delete_an_assigned_task(request, pk=None):
    assign_task = AssignTask.objects.get(id=pk)
    if request.method == "POST":
        assign_task.delete()

    return redirect("assign_task")


# Vista para finalizar una tarea asignada
@login_required(redirect_field_name="login")
def finalize_an_assigned_task(request, pk: None):
    assign_task = AssignTask.objects.get(id=pk)
    if request.method == "POST":
        assign_task.status = "Finalizada"
        assign_task.save()
    
    return redirect("assign_task")


# Vista para actualizar una tarea asignada
@login_required(redirect_field_name="login")
def update_assigned_task(request, pk: None):
    assign_task = AssignTask.objects.get(id=pk)
    if request.method == "POST":
        team_member = TeamMember.objects.get(name=request.POST.get("assignedTo"))
        department = Department.objects.get(name=request.POST.get("department"))

        assign_task.title = request.POST.get("taskName")
        assign_task.description = request.POST.get("taskDescription")
        assign_task.status = request.POST.get("taskStatus")
        assign_task.priority = request.POST.get("taskPriority")
        assign_task.due_date = request.POST.get("dueDate")
        assign_task.team_member = team_member
        assign_task.department = department

        assign_task.save()

        messages.success(request, "Tarea actualizada con exito!")

    return redirect("assign_task")


