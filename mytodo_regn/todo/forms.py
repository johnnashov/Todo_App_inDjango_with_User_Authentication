from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from todo.models import *

class CreateUserForm(UserCreationForm):
  class Meta:
    model = User
    fields = ['username', 'email', 'password1', 'password2'] 


class CreateTodo(ModelForm):
  class Meta:
    model = CustomerToDoItem
    fields = '__all__'
    exclude = ['user']
