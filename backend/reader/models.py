from django.contrib.auth.models import User
from django.db import models
from django.db.models import ForeignKey, DateTimeField, TextField
from backend.localusers.models import LocalUser
from django_counter_field import CounterField
from django_counter_field import CounterMixin, connect_counter


class User(models.Model):
    user = ForeignKey(LocalUser, related_name='reader', on_delete=models.CASCADE)

class Task(models.Model):
    doing = models.CharField(max_length=140)
    notdoing = models.CharField(max_length=140)
    timestamp = DateTimeField(auto_now_add=True)

class HabitCounter(CounterMixin, models.Model):
    #increment each time task is completed
    habitcount = CounterField()
    connect_counter('habitcount', HabitCounter.Task)
    