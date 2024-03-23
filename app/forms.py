from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

class login_form(AuthenticationForm):
    pass

class signup_form(UserCreationForm):
    class Meta:
        model = User
        fields = ['username']