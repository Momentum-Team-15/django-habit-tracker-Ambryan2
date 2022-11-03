
from django.shortcuts import render, get_object_or_404, redirect
from django.db import IntegrityError
from .models import User, Habit, Record, Date, Year, Month, Day
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .forms import HabitForm, RecordEditForm, DateForm, NewRecordForm

# Create your views here.

# want a home page will need login required 
@login_required
def index(request):
    habits = Habit.objects.filter(user=request.user)
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

            # if integrity error occurs then return to same page. Also be sure you are interpreting the right integrityerror
            try:
                record.save()
                return redirect('home')
            except IntegrityError:
                # repeat line 100 and add error message (div)
                return render(request, 'habit/new_record.html', {'form': form, 'form2':form2, 'habit':habit})
    else:
        form = NewRecordForm()
        form2 = DateForm()
    return render(request, 'habit/new_record.html', {'form': form, 'form2':form2, 'habit':habit})

# Need to be able to delete a record 
def record_delete(request, recordpk):
    record = Record.objects.get(pk=recordpk)
    record.delete()
    return redirect('home')

# need to be able to delete a habit
def habit_delete(request, habitpk):
    habit = Habit.objects.get(pk=habitpk)
    habit.delete()
    return redirect('home')


#Need a record to be made every day
#TODO somewhere I need to change the boolean value to determine if record of habit met goal