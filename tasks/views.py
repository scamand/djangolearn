# tasks\views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Task
from .forms import TaskForm

# Create your views here.

# 创建任务
def task_create(request):
    # 如果是POST请求，通过request.POST获取表单数据
    if request.method == 'POST':
        # 将用户提交的数据与TaskForm表单绑定
        form = TaskForm(request.POST)
        # 表单验证
        if form.is_valid():
            # 如果表单有效，保存数据
            form.save()
            # 重定向到任务列表
            return redirect(reverse('tasks:task_list'))

    else:
        # 否则，创建一个空表单
        form = TaskForm()

    # 渲染表单
    return render(request, 'tasks/task_form.html', {'form': form, })

# 取得任务列表
def task_list(request):
    # 从数据库获取Task对象列表
    task = Task.objects.all()
    # 指定渲染模板并向模板传递数据
    return render(request, "tasks/tasks_list.html", {"tasks": task, })


# 取单个任务
def task_detail(request, pk):
    # 从url里获取单个任务的pk值，然后查询数据库获得单个对象
    task = get_object_or_404(Task, pk=pk)
    return render(request, "tasks/task_detail.html", {"task": task, })

# 更新任务
def task_update(request, pk):
    # 从url里获取单个任务的pk值，然后查询数据库获得单个对象实例
    task_obj = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        form = TaskForm(instance=task_obj, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("tasks:task_detail", args=[pk, ]))
        
    else:
        form = TaskForm(instance=task_obj)
    return  render(request, "tasks/task_form.html", {"form": form, "object": task_obj})
    
# 删除任务
def task_delete(request, pk):
    # 从url里获取单个任务的pk值，然后查询数据库获得单个对象
    task_obj = get_object_or_404(Task, pk=pk)
    task_obj.delete() # 删除然后跳转
    return redirect(reverse("tasks:task_list"))


