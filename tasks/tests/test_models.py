from django.test import TestCase
from tasks.models import TasksManagement


# Clase para testear la gestion de tareas de los usuarios - Unit Testing
class TestTasksManagementModel(TestCase):
    print("\n \n \n \t \t \t----------------------------------- Pruebas de software del modulo tasks - proyecto ADSO ---------------------------------")
    def setUp(self) -> None:
        # Tarea de prueba: 1
        self.new_task = TasksManagement.objects.create(
            title = "Actualizar registro del nuevo cliente.",
            description = "Actualizar el estado actual del nuevo cliente",
            priority = "ALTA",
            is_finished = False,
            status = "En proceso",
            due_date = "2024-04-10",
            created_at = "2024-03-23"
        )

        self.new_task.save()

        # Tarea de prueba: 2
        self.new_task_two = TasksManagement.objects.create(
            title = "Acodar reunion con los stakeholders",
            description = "Llevar a cabo una reunion con el equipo y los stakeholders para debatir sobre los requerimientos del cliente ",
            priority = "ALTA",
            is_finished = False,
            status = "En proceso",
            due_date = "2024-05-13",
            created_at = "2024-03-23"
        )

        self.new_task_two.save()

        # Tarea de prueba: 2
        self.new_task_three = TasksManagement.objects.create(
            title = "Reporte de ventas de los ultimos 7 dias",
            description = "Generar el reporte de ventas de las ventas de los productos de hardware de comunicacion.",
            priority = "MEDIA",
            is_finished = False,
            status = "En proceso",
            due_date = "2024-03-30",
            created_at = "2024-03-23"
        )

        self.new_task_three.save()


    def test_number_of_tasks(self):
        # El numero total de tareas agregadas a la base de datos: 3
        show_all_tasks = TasksManagement.objects.all()
        self.assertEquals(show_all_tasks.count(), 3, msg="Comprobar el numero de tareas agregadas a la base de datos.")


    def test_task_length(self):
        # La longitud maxima de caracteres para el campo "title" es de 50.
        length_title = len(self.new_task.title)
        self.assertEquals(length_title, 38, msg="Comprobar que la longitud del titulo de la tarea es correcta." )
        

    def test_task_length_fail(self):
        # hacer fallar la prueba cuando la longitud de caracteres del campo "title" sea mayor a 50.
        length_title = len(self.new_task.title)
        self.assertNotEquals(length_title, 51, msg="Comprobar que la longitud de caracteres del titulo sobrepasa los 50.")
  

    def test_get_task_by_id(self):
        # Obtener una tarea por medio de su ID.
        get_task_by_id = TasksManagement.objects.get(id=self.new_task.id)
        self.assertEquals(get_task_by_id, self.new_task, msg="Comprobar que el ID de una tarea es correcto.")
        

    def test_get_task_by_id_fail(self):
        # Hacer fallar la prueba al obtener una tarea por un ID erroneo.
        get_task_by_id = TasksManagement.objects.get(id=self.new_task.id)
        self.assertNotEquals(self.new_task_three, get_task_by_id, msg="Comprobar que el ID no pertenece a una tarea en especifico.") 


    def test_description_task_label(self):
        # Comporbar que el nombre de una columna es correcto.
        get_task = TasksManagement.objects.get(pk=2)
        get_label_name = get_task._meta.get_field("description").verbose_name
        self.assertEquals(get_label_name, "description", msg="Comprobar que el nombre de la columna de una tarea es la correcta.")