from rest_framework import serializers
from habit.models import Habit

class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = ['id','action', 'target', 'user', 'measurement']
