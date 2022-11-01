from django.contrib import admin
from .models import User, Habit, Record, Date, Year, Month, Day

# Register your models here.
admin.site.register(User)
admin.site.register(Habit)
admin.site.register(Record)
admin.site.register(Date)
admin.site.register(Year)
admin.site.register(Month)
admin.site.register(Day)