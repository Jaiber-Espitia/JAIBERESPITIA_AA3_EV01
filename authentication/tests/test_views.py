from django.test import TestCase, Client
from django.urls import reverse


# Testear las vistas (Interfaz de usuario)
class TestViewHome(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.url = reverse("home")
        self.url_register = reverse("register")
        self.url_login = reverse("login")
        self.response = self.client.get(self.url)
        self.response_login = self.client.get(self.url_login)
        self.response_register = self.client.get(self.url_register)


    def test_home_view_returns_200_ok(self):
        self.assertEquals(self.response.status_code, 200, msg="La vista 'home' debe retornar un codigo de estado 200.")
    

    def test_view_home_fail(self):
        self.assertNotEquals(self.response.status_code, 404, msg="La vista 'home' debe retornar un codigo de estado 400.")


    def test_template_associated_to_url_pass(self):
        # Comprobar los templates y las url asociadas.
        self.assertTemplateUsed(self.response, "base.html")

    
    def test_template_not_associated_to_url_fail(self):
        # Comprobar que la urlno esta asciada al template "menu.html"
        self.assertTemplateNotUsed(self.response, "menu.html")


    def test_context_template_register(self):
        #testing the context inside the template register.
        self.assertIn("form", self.response_register.context)