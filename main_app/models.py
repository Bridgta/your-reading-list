from django.db import models
from django.urls import reverse
from datetime import date

CHAPS = (
        ('1', '< 1 Chapter'),
        ('2', '1-2 Chapters'),
        ('3', '3+ Chapters')
)

class Note(models.Model):
        quote = models.CharField(max_length=100)

        def __str__(self):
                return self.name

        def get_absolute_url(self):
                return reverse('notes_detail', kwargs={'pk': self.id})

class Reading(models.Model):
        title = models.CharField(max_length=100)
        author = models.CharField(max_length=100)
        description = models.TextField(max_length=300)
        pages = models.IntegerField()
        notes = models.ManyToManyField(Note)

def __str__(self):
        return self.name

def get_absolute_url(self):
        return reverse('detail', kwargs={'reading_id': self.id})

def read_for_today(self):
        return self.read_set.filter(date=date.today()).count() >= len(CHAPS)

class Read(models.Model):
        date = models.DateField('Reading date')
        chapter = models.CharField(
                max_length=1,
                choices=CHAPS,
                default=CHAPS[0][0]
        )
        reading = models.ForeignKey(Reading, on_delete=models.CASCADE)

def __str__(self):
        # Nice method for obtaining the friendly value of a Field.choice
        return f"{self.get_chapter_display()} on {self.date}"


class Meta:
        ordering = ['-date']


