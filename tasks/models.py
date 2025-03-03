from django.db import models
from django.utils import timezone

# Create your models here.
class Status(models.TextChoices):
    UNSTARTED = 'UN', 'Unstarted'
    ONGOING = 'OG', 'Ongoing'
    FINISHED = 'FI', 'Finished'

class TimeChooes(models.TextChoices):
    pass


# Task model
class Task(models.Model):
    name = models.CharField(verbose_name='Task Name', max_length=100, unique=True)
    status = models.CharField(verbose_name='Task Status', max_length=2, choices=Status.choices, default=Status.UNSTARTED)
    start_time = models.DateTimeField(verbose_name='Start Time', default=timezone.now, null=True, blank=True)
    # 后面加一个 持续时间 的选项，这样短期任务可以选持续时间，长期任务可以选截止时间
    deadline = models.DateTimeField(verbose_name='Deadline', null=True, blank=True)

    def __str__(self):
        return self.name
 