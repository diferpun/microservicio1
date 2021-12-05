from rest_framework import serializers
from rest_framework.utils import field_mapping
from authApp  import models
from authApp.models.user   import User
from authApp.models.auction import Auction,Bid


class AuctionSerializer(serializers.ModelSerializer):
      class Meta:
          model=Auction
          fields = ['auction_id','product','base_offer','time_starting','time_ending']
          
          
class BidSerializer(serializers.ModelSerializer):
      class Meta:
          model=Bid
          fields = ['bid_id','user','offer','auction','bid_time']