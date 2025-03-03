# tasks\forms.py

from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"
        widgets = {
            'deadline': forms.DateTimeInput(attrs={'id': 'id_deadline', 'class': 'form-control'}),
        }
