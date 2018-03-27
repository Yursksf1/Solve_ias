import datetime

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

CHOICE_PRYORITY = (
    ('1', 'SuperHigh'),
    ('2', 'High'),
    ('3', 'Medium'),
    ('4', 'Minimal'),
    ('5', 'Low'),
)

CHOICE_TYPE = (
    ('1', 'Task'),
    ('2', 'Meeting'),
)

class Task(models.Model):
    check = models.BooleanField(default=False)
    name = models.CharField(max_length=200)
    user = models.ForeignKey(User,
                                models.SET_NULL,
                                blank=True,
                                null=True,
                            )
    type_task = models.CharField(max_length=1,
                                  choices=CHOICE_TYPE,
                                  default=1)
    priority = models.CharField(max_length=1,
                                  choices=CHOICE_PRYORITY,
                                  default=5)
    observation = models.CharField(max_length=200)
    deadline = models.DateTimeField('date finish')

    def __str__(self):
        return self.name

    def is_pending(self):
        return not self.check
    is_pending.boolean = True


   
    


