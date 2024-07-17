from django.db import models


# Create your models here.
class TasksManagement(models.Model):

    class Priority(models.TextChoices):
        NORMAL = "NORMAL", "N"
        MEDIANA = "MEDIANA", "M"
        ALTA = "ALTA", "A"


    title = models.CharField("task title", max_length=50, null=False)
    description = models.TextField("description", max_length=200)
    priority = models.CharField(max_length=10, choices=Priority.choices, default=Priority.NORMAL)
    is_finished = models.BooleanField(default=False)
    status = models.CharField(max_length=15, null=True, blank=True)
    due_date = models.DateField(null=True)
    created_at = models.DateField("date", null=True, auto_now_add=True)


    def __str__(self):
        return self.title
    

    class Meta:
        ordering = ["-created_at", "-title"]
        verbose_name_plural = "Tasks"


# ---------------------------------- Asignar tasks ------------------------------------------


# Modelo de miembro del equipo
class TeamMember(models.Model):
    name = models.CharField("Nombre", max_length=30, null=False, blank=False)


    def __str__(self):
        return self.name
    

    class Meta:
        ordering = ["-name"]
        verbose_name_plural = "TeamMembers"


# Modelo del departamento al que pertenece el miembro del equipo
class Department(models.Model):
    name = models.CharField("Departamento", max_length=25, null=False, blank=False)


    def __str__(self):
        return self.name


    class Meta:
        ordering = ["-name"]
        verbose_name_plural = "Departments"


# Modelo de asignacion de tareas
class AssignTask(models.Model):

    class Priority(models.TextChoices):
        NORMAL = "Normal", "N"
        MEDIANA = "Mediana", "M"
        ALTA = "Alta", "A"


    title = models.CharField("task title", max_length=50, null=False)
    description = models.TextField("description", max_length=200)
    priority = models.CharField(max_length=10, choices=Priority.choices, default=Priority.NORMAL)
    status = models.CharField(max_length=15, null=True, blank=True)
    due_date = models.DateField(null=True)
    created_at = models.DateField("date", null=True, auto_now_add=True)
    team_member = models.ForeignKey(TeamMember, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)


    def __str__(self):
        return str(self.team_member.name)
    

    class Meta:
        ordering = ["-title"]
        verbose_name_plural = "AssignTasks"