
from .models import Habit, Record, Date
from django import forms

class HabitForm(forms.ModelForm):

    class Meta:
        model = Habit
        fields = ('action', 'target','measurement',)

class RecordEditForm(forms.ModelForm):

    class Meta:
        model = Record
        fields = ('target',)

class DateForm(forms.ModelForm):

    class Meta:
        model = Date
        fields = ('h_year','h_month','h_day',)

class NewRecordForm(forms.ModelForm):

    class Meta:
        model = Record
        fields = ('r_habit','target','h_date')
