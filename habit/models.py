from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    pass

class Habit(models.Model):
    action = models.CharField(max_length=50)
    target = models.FloatField()
    measurement = models.CharField(max_length=50, null=True, blank=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE,blank=True, null=True)

    def __str__(self):
        return f"{self.action} for {self.target} {self.measurement}"

class Record(models.Model):
    h_date = models.ForeignKey('Date', on_delete=models.CASCADE,blank=True, null=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE,blank=True, null=True)
    r_habit = models.ForeignKey('Habit', on_delete=models.CASCADE,blank=True, null=True, unique=True)
    outcome = models.BooleanField(default=False)
    target = models.FloatField()

    def __str__(self):
        return f"{self.r_habit} for {self.target}"

class Date(models.Model):
    h_year = models.ForeignKey('Year', on_delete=models.CASCADE,blank=True, null=True, related_name="day")
    h_month = models.ForeignKey('Month', on_delete=models.CASCADE,blank=True, null=True, related_name='day')
    h_day = models.ForeignKey('Day', on_delete=models.CASCADE,blank=True, null=True, related_name='day')

    def __str__(self):
        return f"Year: {self.h_year} Month: {self.h_month} Day: {self.h_day} "

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