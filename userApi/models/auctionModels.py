from django.db import models
from .user     import User
from datetime import timedelta
import datetime

class Auction(models.Model):
       auction_id=models.BigAutoField(primary_key=True)
       product = models.CharField(max_length=50)
       base_offer=models.DecimalField(max_digits=10,decimal_places=2)
       time_starting = models.DateTimeField(default=datetime.date.today)
       time_ending = models.DateTimeField(null=True,default=None)

class Bid(models.Model):
       bid_id = models.BigAutoField(primary_key=True)
       user = models.ForeignKey(User, on_delete=models.CASCADE)
       auction = models.ForeignKey(Auction, on_delete=models.CASCADE)
       offer=models.DecimalField(max_digits=10,decimal_places=2)
       bid_time = models.DateTimeField(default=datetime.date.today)

