from django.shortcuts import render, redirect
from .models import Task

# Create your views here.
def homepage(request):
    task_titles = Task.objects.values('title')
    context = {'task_titles' : task_titles}
    return render(request, 'home.html', context)

def taskpage(request):
    if request.method == 'POST':
        status = request.POST.get('status')
        title = request.POST.get('title')
        body = request.POST.get('body')
        Task.objects.create(
            title = title,
            body = body,
            status = status
        )
        return redirect('task')
    tasks = Task.objects.all()
    context = {'tasks' : tasks}
    return render(request, 'task.html', context)