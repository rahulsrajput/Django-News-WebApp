from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from .models import Article
from django import forms 
from tinymce.widgets import TinyMCE


class login_form(AuthenticationForm):
    pass

class signup_form(UserCreationForm):
    class Meta:
        model = User
        fields = ['username']

class TinyMCEWidget(TinyMCE): 
    def use_required_attribute(self, *args): 
        return False

class add_post_form(forms.ModelForm):
    description = forms.CharField( 
        widget=TinyMCEWidget( 
            attrs={'required': False, 'cols': 30, 'rows': 10, 'id':"mytextarea"} 
        ) 
    ) 
    class Meta:
        model = Article
        fields = ['title','description','image','category','user']

