from typing import ClassVar
from django.conf                             import settings
from rest_framework                          import status, views
from rest_framework.response                 import Response
from rest_framework_simplejwt.serializers    import TokenObtainPairSerializer
from userApi.serializers.userSerializer      import UserSerializer
from rest_framework                          import generics, status
from rest_framework.permissions              import IsAuthenticated
from rest_framework_simplejwt.backends       import TokenBackend
from userApi.models.auctionModels            import Bid,Auction
from userApi.serializers.auctionSerializers  import BidSerializer,AuctionSerializer 
from rest_framework.exceptions               import PermissionDenied


class AuctionCreateview(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = AuctionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response("Auction was created", status=status.HTTP_201_CREATED)