#views.py is your controller(what controls what you see in the webpage)
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import FormView


from .forms import TaskForm

tasks = []

def index(request):
    return HttpResponse("Hello World! This came from the index")

def task_list(request):

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            tasks.append((form.cleaned_data['task_name'], form.cleaned_data['task_date']) )
            return redirect('/blogpage/list/')
        
    elif request.method == 'UPDATE':
        pass
    else:
        form = TaskForm()

    return render(request, "blogpage/task_list.html", 
        {"form": form, 
         "tasks": tasks,
        }
    )

class TaskAddView(FormView):
    template_name = "blogpage/task_add.html"
    form_class = TaskForm
    success_url = "/blogpage/list/"

    def form_valid(self, form):
        tasks.append((form.cleaned_data['task_name'], form.cleaned_data['task_date']) )
        return super().form_valid(form)
