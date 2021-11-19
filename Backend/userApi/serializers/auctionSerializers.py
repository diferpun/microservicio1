from rest_framework import serializers
from rest_framework.utils   import field_mapping
from userApi import models
from userApi.models.user    import User



class AuctionSerializer(serializers.ModelSerializer):
      class Meta:
          model=User
          fields = ['auction_id', 'product_id ', 'time_starting','time_ending']
          
          
       