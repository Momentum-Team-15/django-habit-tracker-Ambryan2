from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


# Create your models here.
class User(AbstractUser):
    pass
# referenced in Record and is connected to user
class Habit(models.Model):
    action = models.CharField(max_length=50)
    target = models.FloatField()
    measurement = models.CharField(max_length=50, null=True, blank=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE,blank=True, null=True)

    def __str__(self):
        return f"{self.action}"

class Record(models.Model):
    h_date = models.ForeignKey('Date', on_delete=models.CASCADE,blank=True, null=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE,blank=True, null=True)
    r_habit = models.ForeignKey('Habit', on_delete=models.CASCADE,blank=True, null=True)
    outcome = models.BooleanField(default=False)
    target = models.FloatField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['h_date','r_habit'], name='habit_per_date')
        ]


    def __str__(self):
        return f"{self.r_habit} for {self.target}"
# the date model is connected to year, month and day and is referenced in Record
class Date(models.Model):
    h_year = models.ForeignKey('Year', on_delete=models.CASCADE,blank=True, null=True, related_name="day")
    h_month = models.ForeignKey('Month', on_delete=models.CASCADE,blank=True, null=True, related_name='day')
    h_day = models.ForeignKey('Day', on_delete=models.CASCADE,blank=True, null=True, related_name='day')
    
    def __str__(self):
        return f"{self.h_year}/{self.h_month}/{self.h_day}"

class Year(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.name}"

class Month(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.name}"


class Day(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.name}"