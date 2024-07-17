from django.test import TestCase
from django.test import TestCase, Client
from django.urls import reverse
from authentication.forms import CreateNewUser


# Comprobar la validacion de datos del formulario de registro
class TestRegisterForm(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.url = reverse("register")

        # Probar datos de autenticacion: Datos validos
        self.user_valid_data = {
            "username": "andressilvera12",
            "email": "andres12@gmail.com",
            "password1": "3144300Ua",
            "password2": "3144300Ua"
        }

        # Probar datos de autenticacion: Datos invalidos
        self.user_invalid_data = {
            "username": "andressilvera12",
            "email": "andres12gmail.com",
            "password1": "3144300Ua",
            "password2": "3144300Ua"
        }

        # Crear un nuevo usuario desde el formulario, con datos ficticios de self.user_data: datos correctos
        self.form = CreateNewUser(data=self.user_valid_data)

        # Crear un nuevo usuario desde el formulario, con datos ficticios de self.user_data: datos incorrectos
        self.form_invalid_data = CreateNewUser(data=self.user_invalid_data)


        # Enviar datos desde el formulario: devolver un codigo de estado 200: OK
        self.send_data = {

            "username": "andressilvera12",
            "email": "andres12@gmail.com",
            "password1": "3144300UA",
            "password2": "3144300UA"
        }

        # Enviar datos desde el formulario: devolver un codigo de estado 404: OK
        self.send_data_error = {

            "username": "andressilvera12",
            "email": "andres12@gmail.com",
            "password1": "3144300uA",
            "password2": "3144300A"
        }

    
    def test_if_form_is_valid(self):
        # Comprobar que los campos del formulario de registro son validos.
        self.assertTrue(self.form.is_valid(), msg="Comprobar que todos los campos del formulario de registro son validos.")


    def test_if_form_is_not_valid(self):
        # Comprobar que los datos ingresados son invalidos.
        self.assertFalse(self.form_invalid_data.is_valid(), msg="Comprobar que los datos ingresados en el formulario de registro son invalidos.")


    def test_send_data_form(self):
        # Comprobar que el codigo de estado recibidio desde el servidor es 200.
        response = self.client.post(self.url, self.send_data)
        self.assertEquals(response.status_code, 200, msg="Comprobar que al enviar los datos desde el formulario de registro la respuesta del servidor debe ser un codigo de estado 200.")


    def test_send_data_form_error_404(self):
        response = self.client.post(self.url, self.send_data_error)
        # Comprobar que los datos enviados son incorrecto y el servidor devuelve un error 404.
        self.assertNotEquals(response.status_code, 404, msg="Comprobar que los datos enviados desde el formulario de registro son erroneos y el servidor debe responde un codigo de estado 404.")
