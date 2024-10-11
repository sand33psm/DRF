from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(max_length=260)
    completed = models.BooleanField(default=False)
    due_date = models.DateField()

    def __str__(self):
        return self.title
    