from datetime import datetime
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class TaskGroup(models.Model):
    name = models.CharField(max_length = 50)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('blogpage:task_list', args=[str(self.pk)])
    
    @property
    def is_due(self):
        return datetime.now() >= self.due_date

    class Meta:
        ordering = ['name'] #order by due date ascending order
        verbose_name = 'task group'
        verbose_name_plural = 'task groups'

class Profile (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    year = models.IntegerField()
    course = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username
    
class Task(models.Model):
    name = models.CharField(max_length = 100)
    due_date = models.DateTimeField(null = False)
    taskgroup = models.ForeignKey(TaskGroup, on_delete=models.CASCADE, related_name = "tasks")
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='task_list',null=True, blank=True)

    def __str__(self):
        return '{}: due on {} unit(s)'.format(self.name, self.due_date)
    
    def get_absolute_url(self):
        return reverse('blogpage:task_detail', args=[str(self.pk)])
    
    @property
    def is_due(self):
        return datetime.now() >= self.due_date
    
    class Meta:
        ordering = ['due_date'] #order by due date ascending order
        unique_together = ['due_date', 'name'] #to avoid duplicate tasks
        verbose_name = 'task'
        verbose_name_plural = 'tasks'
