
from .models import Habit, Record, Date
from django import forms

class HabitForm(forms.ModelForm):

    class Meta:
        model = Habit
        fields = ('action', 'target','measurement',)
        labels = {
            'action':'New Habit ',
            'target':'How much or How long? ',
            'measurement':'By what metric? '
        }

class RecordEditForm(forms.ModelForm):

    class Meta:
        model = Record
        fields = ('target',)
        labels = {
            'target':'Record amount'
        }

class DateForm(forms.ModelForm):

    class Meta:
        model = Date
        fields = ('h_year','h_month','h_day',)
        labels = {
            'h_year':'Year ',
            'h_month':'Month ',
            'h_day':'Day '
        }

class NewRecordForm(forms.ModelForm):

    class Meta:
        model = Record
        fields = ('target','h_date')
        labels = {
            'target': 'Record Amount',
            'h_date':'Existing Date'
        }
