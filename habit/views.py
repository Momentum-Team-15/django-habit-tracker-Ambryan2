from signal import pause
from django.shortcuts import render, get_object_or_404, redirect
from .models import User, Habit, Record, Date, Year, Month, Day
from django.db.models import Q
from .forms import HabitForm, RecordForm

# Create your views here.

# want a home page will need login required 
def index(request):
    habits = Habit.objects.all()
    return render(request, 'habit/index.html', {'habits':habits})

# want a login page
# want a view for all particular habit records, if there are no record send them to page to add records
def habit_detail(request, pk):
    records = Record.objects.filter(r_habit=pk).order_by('-h_date')
    return render(request,'habit/habit_detail.html',{'records':records})

#want a view of each individual record for a set date with url 
def day_record(request, habitpk, yearpk, monthpk, daypk):
    year = Year.objects.get(name=yearpk)
    month = Month.objects.get(pk=monthpk)
    day = Day.objects.get(name=daypk)
    date = Date.objects.get(h_year=year,h_month=month,h_day=day)
    records = Record.objects.filter(r_habit=habitpk,h_date=date)
    return render(request,'habit/day_record.html',{'records':records})

#want a way to add habits (need a form)
def habit_new(request):
    if request.method == "POST":
        form = HabitForm(request.POST)
        if form.is_valid():
            # this is save an instance of album in database. Commit=False is only needed if we need to add user
            habit = form.save(commit=False)
            habit.user = request.user
            habit.action = habit.action.lower()
            habit.save()
            return redirect('home') 
    else:
        form = HabitForm()
    return render(request, 'habit/habit_edit.html', {'form': form})
#Able to edit records
def edit_records(request, habitpk, datepk):
    record = Record.objects.get(r_habit=habitpk,h_date=datepk)
    if request.method == "POST":
        form = RecordForm(request.POST, instance=record)
        if form.is_valid():
            record = form.save(commit=True)
            record.save()
            return redirect('home')
    else:
        form = RecordForm(instance=record)
    return render(request, 'habit/record_edit.html', {'form': form})


#Need a record to be made every day
#TODO somewhere I need to change the boolean value to determine if record of habit met goal