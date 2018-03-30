import datetime

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models import Q
from django.core.exceptions import ValidationError

from django.http import Http404
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

def getLazyTime(total_sec):
    dias_delta = 60*60*24
    dias = total_sec // dias_delta
    if dias:
        return str(dias) + ' d' 
    
    hora_delta = 60*60
    total_sec = total_sec - dias*dias_delta
    horas = total_sec // hora_delta    
    if horas:
        return str(horas) + ' h'
    
    minu_delta = 60
    total_sec = total_sec - horas*hora_delta
    minutes = total_sec // minu_delta
    if minutes:
        return str(minutes) + ' m'

    total_sec = total_sec - minutes*minu_delta
    sec = total_sec    
    if sec:
        return str(sec) + ' s'
    return 'now'

class Task(models.Model):
    check = models.BooleanField("Terminado", default=False)
    name = models.CharField("Nombre de Tarea", max_length=200)
    user = models.ForeignKey(User,
                                models.SET_NULL,
                                blank=True,
                                null=True,
                            )
    type_task = models.CharField("Tipo de Tarea", max_length=1,
                                  choices=CHOICE_TYPE,
                                  default=1)
    priority = models.CharField("Prioridad", max_length=1,
                                  choices=CHOICE_PRYORITY,
                                  default=5)
    observation = models.CharField("Observación", max_length=200, blank=True)
    date_start = models.DateTimeField('Fecha de Inicio', default=timezone.now())
    date_end = models.DateTimeField('Fecha de Finalización', default=timezone.now() + datetime.timedelta(minutes=30) )

    def __str__(self):
        return self.name

    def is_pending(self):
        return not self.check
    is_pending.boolean = True

    def duration_lazy(self):
        total_sec = (self.date_end - self.date_start).total_seconds()
        duration = getLazyTime(total_sec)
        return duration    

    def duration(self):
        total_sec = (self.date_end - self.date_start).total_seconds()
        return total_sec
    #duration = datetime.timedelta(minutes=30).total_seconds()

    def save(self, *args, **kwargs):
        if self.date_start<self.date_end:
            super(Task, self).save(*args, **kwargs) # Call the "real" save() method.
        else: 
            raise ValidationError("Overlapping dates")
        



