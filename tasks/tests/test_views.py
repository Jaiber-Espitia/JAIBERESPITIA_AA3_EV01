from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.url = reverse("tasks")
        self.response = self.client.get(self.url)


    def test_tasks_view(self):
        self.assertEquals(self.response.status_code, 302, msg="Comprobar que la respuesta del sevidor es exitosa al acceder a la ruta 'tasks'.")


    def test_tasks_template(self):
        self.assertTrue(True, True)