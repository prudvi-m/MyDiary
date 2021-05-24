from rest_framework import serializers
from .models import Diary

class DiarySerializer(serializers.ModelSerializer):
    class Meta:
       model =Diary 
       fields = ("id","voice_text","file_name","created_at","is_file","text")
       