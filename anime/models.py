
from django.db import models

# Create your models here.
class animecards(models.Model):
    a_photo=models.FileField(upload_to='cardmedia/',max_length=400,null=True,default=None)
    a_title=models.CharField(max_length=100)
    a_descript=models.CharField(max_length=1000)
    a_link=models.CharField(max_length=100,default=None)
