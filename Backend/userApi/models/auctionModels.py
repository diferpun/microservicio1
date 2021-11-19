from django.db import models
from .user     import User

class Auction(models.Model):
       auction_id=models.BigAutoField(primary_key=True)
       product_id = models.IntegerField()
       time_starting = models.DateTimeField()
       time_ending = models.DateTimeField()

class Bid(models.Model):
       
       bid_id = models.BigAutoField(primary_key=True)
       auction_id = models.ForeignKey(Auction, on_delete=models.CASCADE)
       bid_time = models.DateTimeField()

