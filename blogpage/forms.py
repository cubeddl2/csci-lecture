from django import forms

class TaskForm(forms.Form):
    task_name = forms.CharField()
    task_date = forms.DateField()
    