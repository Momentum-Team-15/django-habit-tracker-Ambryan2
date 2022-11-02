from .models import Habit, Record
from django import forms

class HabitForm(forms.ModelForm):

    class Meta:
        model = Habit
        fields = ('action', 'target','measurement',)

class RecordForm(forms.ModelForm):

    class Meta:
        model = Record
        fields = ('target',)
