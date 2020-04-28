from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.urls import reverse
from . import models


# Create your views here.

def home(request):
    print('ola1')
    todo_items = models.Todo.objects.all().order_by("-added_date")
    return render(request, 'main/index.html', {"todo_items": todo_items})


def add_todo(request):
    print('ola2')
    current_date = timezone.now()
    content = request.POST["content"]
    created_obj = models.Todo.objects.create(added_date=current_date, text=content)
    lenght_of_todos = models.Todo.objects.all().count()
    return HttpResponseRedirect(reverse('home'))


def delete_todo(request, todo_id):
    print('ola3')
    models.Todo.objects.filter(id=todo_id).delete()
    return HttpResponseRedirect(reverse('home'))
