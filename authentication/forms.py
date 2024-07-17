from django import forms
from django.contrib.auth.forms import UserCreationForm, SetPasswordForm
from django.contrib.auth.models import User


class CreateNewUser(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        super(CreateNewUser, self).__init__(*args, **kwargs)

        self.fields["username"].widget.attrs.update({
            "class": "form-control form-control-lg",
            "placeholder": "Nombre de usuario",
            "id": "typeUsername"
            })
        
        self.fields["email"].widget.attrs.update({
            "class": "form-control form-control-lg", 
            "placeholder": "Email", 
            "id": "typeEmail"
            })
        
        self.fields["password1"].widget.attrs.update({
            "class": "form-control form-control-lg", 
            "placeholder": "Contraseña", 
            "id": "typePasswor1"
            })
        
        self.fields["password2"].widget.attrs.update({
            "class": "form-control form-control-lg", 
            "placeholder": "Repita su contraseña", 
            "id": "typePassword2"
            })


# Restablecer contraseña
class ChangePasswordForm(SetPasswordForm):
    class Meta:
        model = User
        fields = ["new_password1", "new_password2"]

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super().__init__(user, *args, **kwargs)

        self.fields['new_password1'].widget.attrs.update({
            'id': 'new_password1', 
            'required': True,
            'class': 'form-control mb-4', 
            'placeholder': "Ingrese su nueva contraseña",
            'autocomplete': "Contraseña del usuario",
            })
        
        self.fields['new_password2'].widget.attrs.update({
            'id': 'new_password2', 
            'class': 'form-control', 
            'required': True,
            'placeholder': "Confirme su nueva contraseña",
            'autocomplete': "Contraseña del usuario",
            })