from rest_framework                   import serializers
from rest_framework.utils             import field_mapping
from userApi                          import models
from userApi.models.user              import User
from userApi.models.auctionModels     import Auction,Bid


class AuctionSerializer(serializers.ModelSerializer):
      class Meta:
          model=Auction
          fields = ['auction_id', 'product', 'time_starting','time_ending']
          
          
class BidSerializer(serializers.ModelSerializer):
      class Meta:
          model=Bid
          fields = ['bid_id','user','auction','bid_time']
                    
 