from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class TaskCategory(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Task(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks_created')
    assignees = models.ManyToManyField(User, related_name='tasks_assigned', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()
    points = models.IntegerField()
    approvers = models.ManyToManyField(User, related_name='tasks_approvable', blank=True)
    category = models.ForeignKey(TaskCategory, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class Mission(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    tasks = models.ManyToManyField(Task, blank=True)
    point_reward = models.IntegerField(default=0)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name
