from django.shortcuts import render, get_object_or_404
from .models import User, Habit, Record, Date
from django.db.models import Q

# Create your views here.

# want a home page will need login required 
def index(request):
    habits = Habit.objects.all()
    return render(request, 'habit/index.html', {'habits':habits})

# want a login page
# want a view for all particular habit records, if there are no record send them to page to add records
def habit_detail(request, pk):
    records = Record.objects.filter(r_habit=pk)
    return render(request,'habit/habit_detail.html',{'records':records})
#want a view of each individual record for a set date with url 
def day_record(request, habitpk, yearpk, monthpk, daypk):
    date = Date.objects.filter(h_day=1)
    record = Record.objects.filter(
        Q(r_habit=habitpk)
        )
    return render(request,'habit/day_record.html',{'record':record,'date':date})
#want a way to add habits (need a form)
#TODO somewhere I need to change the boolean value to determine if record of habit met goal