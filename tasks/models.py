from django.db import models

# Create your models here.
class Status(models.TextChoices):
    UNSTARTED = 'UN', 'Unstarted'
    ONGOING = 'OG', 'Ongoing'
    FINISHED = 'FI', 'Finished'

# Task model
class Task(models.Model):
    name = models.CharField(verbose_name='Task Name', max_length=100, unique=True)
    status = models.CharField(verbose_name='Task Status', max_length=2, choices=Status.choices, default=Status.UNSTARTED)

    def __str__(self):
        return self.name
    