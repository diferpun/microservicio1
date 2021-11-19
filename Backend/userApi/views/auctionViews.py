import re
from typing import ClassVar
from django.conf                             import settings
from rest_framework                          import serializers, status, views
from rest_framework.exceptions import ValidationError
from rest_framework.response                 import Response
from rest_framework_simplejwt.serializers    import TokenObtainPairSerializer
from userApi.serializers.userSerializer      import UserSerializer
from rest_framework                          import generics, status
from rest_framework.permissions              import IsAuthenticated
from rest_framework_simplejwt.backends       import TokenBackend
from userApi.models.auctionModels            import Bid,Auction
from userApi.serializers.auctionSerializers  import BidSerializer,AuctionSerializer 

class BidCreateview(views.APIView):   
    permission_classes = (IsAuthenticated,)   
    def post(self, request, *args, **kwargs):
        serializer = BidSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token        = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data   = tokenBackend.decode(token,verify=False)
        
        if request.data['user'] != valid_data['user_id']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        serializer.save()
        return Response("Bid was created", status=status.HTTP_201_CREATED)


class BidDetailView(generics.ListAPIView):
    serializer_class   = BidSerializer
    #permission_classes = (IsAuthenticated,)
     
    def get_queryset(self):
        
        token        = self.request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data   = tokenBackend.decode(token,verify=False)
        
        print("hola 1",valid_data['user_id'])
        print("hola 4",self.kwargs["user"])
        
        if valid_data['user_id'] != self.kwargs['user']:
            print("son diferentes")  
            #stringResponse = {'detail':'Unauthorized Request'}
            #return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
            raise ValidationError({"error": ["You don't have enough permission."]}) 
        
        queryset = Bid.objects.filter(user_id=self.kwargs["user"])
        return queryset



class AuctionCreateview(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = AuctionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response("Auction was created", status=status.HTTP_201_CREATED)