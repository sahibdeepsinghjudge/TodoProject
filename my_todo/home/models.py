from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Todo(models.Model):
    title  = models.CharField(max_length=200, blank = False, null = False)
    description = models.TextField(blank = True, null = True)
    is_completed = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,default=1)

    def __str__(self):
        return self.title
