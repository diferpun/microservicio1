from rest_framework                   import serializers
from rest_framework.utils             import field_mapping
from userApi                          import models
from userApi.models.user              import User
from userApi.models.auctionModels     import Auction,Bid


class AuctionSerializer(serializers.ModelSerializer):
      class Meta:
          model=Auction
          fields = ['auction_id','product','base_offer','time_starting','time_ending']
          
          
class BidSerializer(serializers.ModelSerializer):
      class Meta:
          model=Bid
          fields = ['bid_id','user','offer','auction','bid_time']
                    
      def to_representation(self, obj):
          user = User.objects.get(id=obj.user.id)
          auction=Auction.objects.get(auction_id=obj.auction.auction_id)
          bid=Bid.objects.get(bid_id=obj.bid_id)
          
          return{  
                   'bid_id': bid.bid_id,
                   
                   'user':{
                        'id'      :  user.id,  
                        'username':  user.username,    
                        'email'   :  user.email
                   },
                   
                     'auction':{
                        'auction_id'   : auction.auction_id,
                        'product'      : auction.product, 
                        'base_offer'   : auction.base_offer,
                        'time_starting': auction.time_starting,
                        'time_ending'  : auction.time_ending 
                   }, 
                   'offer':     bid.offer,
                   'bid_time':  bid.bid_time 
               }          
 
 
 #'id', 'firstname', 'lastname','username', 'password', 'email', 'isadmi'
 # 'bid_id','user','offer','auction','bid_time'