from django.shortcuts import render
from rest_framework import generics
from .serializers import DiarySerializer
from .models import Diary

class DiaryView(generics.CreateAPIView):
    queryset = Diary.objects.all()
    serializer_class = DiarySerializer