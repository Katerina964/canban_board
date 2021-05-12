from django.db import models
from django.contrib.auth.models import User


class Card(models.Model):
    PLAN = 'P'
    DOING = 'D'
    DONE = 'DN'
    STATE = [(PLAN, 'PLAN'),
             (DOING, 'DOING'),
             (DONE, 'DONE')]
    name = models.CharField(max_length=150)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    state = models.CharField(max_length=2,
                             choices=STATE,
                             default=PLAN)

    def __str__(self):
        return self.name
