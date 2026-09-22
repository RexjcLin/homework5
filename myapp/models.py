from django.db import models

# Create your models here.
#創建一個temperature_db資料庫
class temperature_db(models.Model):
    myid = models.AutoField(primary_key=True)
    sensor_id = models.IntegerField()
    temperature = models.FloatField() 
    humidity = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
