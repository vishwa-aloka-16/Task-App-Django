from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class AppTask(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    deadline = models.DateField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)    

    def __str__(self):
        return self.title
