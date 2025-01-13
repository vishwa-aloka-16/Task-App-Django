from django import forms
from .models import AppTask

class TaskForm(forms.ModelForm):
    class Meta:
        model = AppTask
        fields = ['title', 'description', 'deadline']
        widgets = {
            'deadline': forms.DateTimeInput(attrs={'type': 'date'}),
        }

class TaskFormUpdate(forms.ModelForm):
    class Meta:
        model = AppTask
        fields = ['complete','title', 'description', 'deadline']
        widgets = {
            'deadline': forms.DateTimeInput(attrs={'type': 'date'}),
        }