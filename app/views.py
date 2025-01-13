from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import ListView,CreateView,UpdateView
from .models import AppTask
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import TaskForm,TaskFormUpdate
# Create your views here.

class allTaskListView(LoginRequiredMixin,ListView):
    model = AppTask
    template_name = 'app/task_main.html'
    context_object_name = 'tasks'
    paginate_by = 10
    def get_queryset(self):
        return AppTask.objects.filter(user=self.request.user)

class taskListView(LoginRequiredMixin,ListView):
    model = AppTask
    template_name = 'app/task_list.html'
    context_object_name = 'tasks'
    
    def get_queryset(self):
        return AppTask.objects.filter(user=self.request.user).filter(complete = False)


class CompleteTaskListView(LoginRequiredMixin,ListView):
    model = AppTask
    template_name = 'app/task_Done.html'
    context_object_name = 'tasks'
    
    def get_queryset(self):
        return AppTask.objects.filter(user=self.request.user).filter(complete = True)

class taskCreateView(LoginRequiredMixin,CreateView):
    model = AppTask
    template_name = 'app/task_add.html'
    context_object_name = 'tasks'
    form_class = TaskForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form) 
    
    def get_success_url(self):
        return reverse_lazy('app-home') 

class TaskUpdateView(UpdateView):
    model = AppTask
    template_name = 'app/task_update.html'
    context_object_name = 'tasks'
    form_class = TaskFormUpdate

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form) 
    
    def get_success_url(self):
        return reverse_lazy('app-home') 