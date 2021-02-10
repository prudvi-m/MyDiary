from django.db import models
from django.db.models.expressions import F
import string
import random

def generate_unique_code():
    length =6

    while True:
        code = ''.join(random.choice(string.hexdigits,k=length))

        if Diary.objects.filter(code==code).count() == 0:
            break

    return code

# Create your models here.
class Diary(models.Model):
    code = models.CharField(max_length=8,default="",unique=True)
    voice_text = models.CharField(max_length=500,default="",unique=True)
    file_name = models.CharField(max_length=10,default="",unique=True)
    created_at= models.DateTimeField(auto_now_add=True)
    is_file = models.BooleanField(null=False,default=1)
    text =  models.CharField(max_length=500,default="",unique=True)


    # voice_text,file_name,created_at,is_file,text