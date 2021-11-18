from rest_framework import serializers
from rest_framework.utils   import field_mapping
from userApi.models.user    import User


class UserSerializer(serializers.ModelSerializer):
      class Meta:
          model=User
          fields = ['id', 'firstname', 'lastname','username', 'password', 'email', 'isadmi']
          
    
      
      
       
        
       