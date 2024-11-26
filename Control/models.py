from django.db import models

class LED_States(models.Model):
  LED1 = models.BooleanField()
  LED2 = models.BooleanField()
