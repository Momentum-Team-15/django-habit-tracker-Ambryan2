from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


# Create your models here.
class User(AbstractUser):
    pass
# referenced in Record and is connected to user
class Habit(models.Model):
    action = models.CharField(max_length=50,)
    target = models.FloatField()
    measurement = models.CharField(max_length=50, null=True, blank=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE,blank=True, null=True)
    actual_date = models.DateField(auto_now_add=True, null=True) 

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['action','user'], name='habit_action')
        ]

    def __str__(self):
        return f"{self.action}"

class Record(models.Model):
    h_date = models.ForeignKey('Date', on_delete=models.CASCADE,blank=True, null=True)
    # this user is not needed but i will not touch because it is already in database
    user = models.ForeignKey('User', on_delete=models.CASCADE,blank=True, null=True)
    r_habit = models.ForeignKey('Habit', on_delete=models.CASCADE,blank=True, null=True)
    # this is not needed as a user can change this 
    outcome = models.BooleanField(default=False)
    target = models.FloatField(default=0)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['h_date','r_habit','user'], name='habit_per_date')
        ]

    def __str__(self):
        return f"{self.r_habit} for {self.target}"

# the date model is connected to year, month and day and is referenced in Record
class Date(models.Model):
    h_year = models.ForeignKey('Year', on_delete=models.CASCADE,blank=True, null=True, related_name="dates")
    h_month = models.ForeignKey('Month', on_delete=models.CASCADE,blank=True, null=True, related_name='dates')
    h_day = models.ForeignKey('Day', on_delete=models.CASCADE,blank=True, null=True, related_name='dates')
    
    def __str__(self):
        return f"{self.h_year}/{self.h_month}/{self.h_day}"

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['h_year','h_month','h_day'], name='one_date')
        ]

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