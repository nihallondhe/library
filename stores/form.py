from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import store

from .models import books

class CreatestoreForm(ModelForm):
    class Meta:
        model = store
        fields = '__all__'

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email']

class CreatebooksForm(ModelForm):
    class Meta:
        model = books
        fields = '__all__'
