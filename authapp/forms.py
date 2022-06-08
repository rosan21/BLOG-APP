from django.contrib.auth.models import User
from django.forms import CharField, ModelForm, PasswordInput

class RegisterForm(ModelForm):
    password = CharField(widget=PasswordInput)
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']

class LoginForm(ModelForm):
    password = CharField(widget=PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'password']