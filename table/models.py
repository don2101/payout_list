from django.db import models

# Create your models here.
class Payout(models.Model):
    buyer = models.CharField(max_length=50, blank=False)
    item = models.CharField(max_length=1000, blank=False)
    money = models.IntegerField(blank=False)
    buy_date = models.DateField(blank=False)
    