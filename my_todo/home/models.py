from django.db import models

# Create your models here.


class Todo(models.Model):
    title  = models.CharField(max_length=200, blank = False, null = False)
    description = models.TextField(blank = True, null = True)
    is_completed = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
