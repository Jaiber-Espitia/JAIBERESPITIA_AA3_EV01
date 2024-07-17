from django.test import TestCase
from django.urls import reverse, resolve
from tasks.views import (
    task_manager,
    add_task,
    delete_task,
    update_task
)


class TestUrls(TestCase):
    def setUp(self) -> None:
        # Ruta a la vista de tareas
        self.path_to_tasks = reverse("tasks")
        self.show_tasks = resolve(self.path_to_tasks)

        # ruta a la vista de agregar tareas
        self.path_to_add_tasks = reverse("add")
        self.add_task = resolve(self.path_to_add_tasks)

        # ruta a la vista de eliminar tareas
        self.path_to_delete_tasks = reverse("delete", args=[1])
        self.delete_task = resolve(self.path_to_delete_tasks)

        # ruta a la vista de actualizar tareas
        self.path_to_update_tasks = reverse("update", args=[1])
        self.update_task = resolve(self.path_to_update_tasks)

    
    def test_url_of_task_manager(self):
        # Debe devover la vista que tiene asociada la ruta: tasks
        self.assertEquals(self.show_tasks.func, task_manager, msg="Comprobar que la vista 'task_manager' tiene asociada su correcta ruta.")


    def test_url_of_task_manager_fail(self):
        self.assertNotEquals(self.show_tasks.func, add_task, msg="Comprobar que la vista 'task_manager' no tiene asociada su correcta ruta.")


    def test_url_of_add_task(self):
        self.assertEquals(self.add_task.func, add_task, msg="Comprobar que la vista 'add_task' tiene asociada su correcta ruta.")

    
    def test_url_of_delete_task(self):
        self.assertEquals(self.delete_task.func, delete_task, msg="Comprobar que la vista 'delete_task' tiene asociada su correcta ruta.")


    def test_url_of_update_task(self):
        self.assertEquals(self.update_task.func, update_task, msg="Comprobar que la vista 'update_task' tiene asociada su correcta ruta.")
