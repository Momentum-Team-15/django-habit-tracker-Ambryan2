from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.response import Response
from habit.models import Habit
from .serializers import HabitSerializer

# Create your views here.
class HabitListView(APIView):
    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        # Query for all habits an serialize all the data so I can return habits as json
        habits = Habit.objects.all()
        serializer = HabitSerializer()

        return Response(serializer.data)