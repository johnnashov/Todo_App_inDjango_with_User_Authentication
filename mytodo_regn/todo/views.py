from django.shortcuts import render, redirect
from todo.models import *
from todo.forms import *
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def registerPage(request):
  form = CreateUserForm()

  if request.method == 'POST':
    form = CreateUserForm(request.POST)
    if form.is_valid():
      form.save()
      return HttpResponse('Success')

  context = {'form':form}
  return render(request, 'register.html', context)




def loginPage(request):
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(request, username=username, password=password)

    if user is not None:
      login(request, user)
      return redirect('usertodo')
    else:
      messages.info(request, 'Invalid Credentials')
      return render(request, 'login.html')

  return render(request, 'login.html')



def logoutUser(request):
  logout(request)
  return redirect('login')




@login_required(login_url = 'login')
def userTodo(request):
  todoitems = request.user.customertodoitem_set.all()
  context = {'todoitems':todoitems}

  return render(request, 'todo.html', context)




def index(request):
  return render(request, 'index.html')



@login_required(login_url = 'login')
def addTodo(request):

  if request.method == 'POST':
    user = request.user
    content = request.POST['content']
    priority = request.POST['priority']
    todoitem = CustomerToDoItem.objects.create(user=user, content=content, priority=priority)
    return redirect('usertodo')

  return HttpResponseRedirect('/todo/')




def deleteTodo(request, todo_id):
  item_to_delete = CustomerToDoItem.objects.get(id=todo_id)
  if item_to_delete.user == request.user:
    item_to_delete.delete()
    return HttpResponseRedirect('/todo/')
  else:
    return HttpResponse("You are not authorized to do that !")

  
  