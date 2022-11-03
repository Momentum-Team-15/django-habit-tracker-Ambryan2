
from django.shortcuts import render, get_object_or_404, redirect
from .models import User, Habit, Record, Date, Year, Month, Day
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .forms import HabitForm, RecordEditForm, DateForm, NewRecordForm

# Create your views here.

# want a home page will need login required 
@login_required
def index(request):
    habits = Habit.objects.all()
    return render(request, 'habit/index.html', {'habits':habits})

# want a logout link
def logout(request):
    return render(request, 'accounts/logout/')

# want a view for all particular habit records, if there are no record send them to page to add records
def habit_detail(request, pk):
    habit = Habit.objects.get(pk=pk)
    records = Record.objects.filter(r_habit=pk).order_by('-h_date')
    return render(request,'habit/habit_detail.html',{'records':records,'habit':habit})

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
        form = RecordEditForm(request.POST, instance=record)
        if form.is_valid():
            record = form.save(commit=True)
            record.save()
            return redirect('home')
    else:
        form = RecordEditForm(instance=record)
    return render(request, 'habit/record_edit.html', {'form': form})

# Need to create a new date everyday
def new_date(request):
    pass

# creates a new record, but doesn't have date and it needs that
# TODO: Need to make date show up when it is custom made
def new_record(request, habitpk):
    collection = Record.objects.filter(r_habit=habitpk)
    dates = Date.objects.all()
    habit = Habit.objects.get(pk=habitpk)
    if request.method == "POST":
        form = NewRecordForm(request.POST)
        form2 = DateForm(request.POST)
        if form.is_valid() and form2.is_valid():
            # this is save 
            record = form.save(commit=False)
            date = form2.save(commit=False)
            
            # When record.h_date is filled in it matches a date in dates, so if empty it automatically shouldn't
            if record.h_date not in dates and date not in dates:
                date.save()
                record.h_date = date

            record.r_habit = habit
            record.user = request.user

            if record not in collection:
                record.save()
                return redirect('home')
            else:
                return redirect('home') 
    else:
        form = NewRecordForm()
        form2 = DateForm()
    return render(request, 'habit/new_record.html', {'form': form, 'form2':form2, 'habit':habit, 'collection':collection})
# TODO Maybe a try and catch for the above for IntegrityError so that it doesn't go to error page

#Need a record to be made every day
#TODO somewhere I need to change the boolean value to determine if record of habit met goal