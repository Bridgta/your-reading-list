from django.db import models

class Reading(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    pages = models.IntegerField()


def __str__(self):
        return self.name