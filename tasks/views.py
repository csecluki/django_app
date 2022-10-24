from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect

from tasks.forms import TaskForm
from tasks.models import Task


@login_required
def task_home_view(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'tasks_home.html', context={'tasks': tasks})


def task_add_view(request):
    form = TaskForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        task = form.save(commit=False)
        task.user = request.user
        task.save()
        return redirect('task_home')
    return render(request, 'task_form.html', {'form': form})


def task_modify_view(request, slug):
    task = Task.objects.get(Q(user=request.user), Q(slug=slug))
    form = TaskForm(request.POST or None, instance=task)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('task_home')
    context = {'form': form}
    return render(request, 'task_form.html', context)


def task_remove_view(request, slug):
    if request.method == 'POST':
        task = Task.objects.get(Q(user=request.user), Q(slug=slug))
        task.delete()
        return JsonResponse({'detail': "Success"}, status=200)


def task_change_status_view(request, slug):
    if request.method == 'POST':
        task = Task.objects.get(Q(user=request.user), Q(slug=slug))
        if task.status == 2:
            return JsonResponse({'detail': "Task was already done"}, status=400)
        task.change_status()
        return JsonResponse(
            data={'detail': "Success",
                  'status': task.get_status_display(),
                  'update_date': task.last_update.strftime("%d-%m-%Y %H:%M")},
            status=200
        )
