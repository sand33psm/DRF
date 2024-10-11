from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=120)
    author = models.CharField(max_length=120)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title