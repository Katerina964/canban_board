from django.db import models
from django.contrib.auth.models import User


class Card(models.Model):
    TODO = 'TD'
    DOING = 'D'
    DONE = 'DN'
    STATE = [(TODO, 'TODO'),
             (DOING, 'DOING'),
             (DONE, 'DONE')]
    name = models.CharField(max_length=150, blank=True)
    description = models.TextField(blank=True)
    start_date = models.DateField(blank=True)
    end_date = models.DateField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    state = models.CharField(max_length=2,
                             choices=STATE,
                             default=TODO)

    def __str__(self):
        return self.name
