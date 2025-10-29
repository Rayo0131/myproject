from django.db import models
from django.conf import settings


# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='task')
    title = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title