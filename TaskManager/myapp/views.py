from django.shortcuts import render
from .models import Task

def task_view(request):
    tasks = Task.objects.all()
    context = {
        'tasks': tasks,
    }
    return render(request, 'task.html', context)
