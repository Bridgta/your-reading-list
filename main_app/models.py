from django.db import models

from django.urls import reverse

class Reading(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    pages = models.IntegerField()

def __str__(self):
        return self.name

def get_absolute_url(self):
        return reverse('detail', kwargs={'reading_id': self.id})
