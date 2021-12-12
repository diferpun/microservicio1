from typing import ClassVar
from django.conf                             import settings
from rest_framework                          import status, views
from rest_framework.response                 import Response
from rest_framework                          import generics, status
from rest_framework.permissions              import IsAuthenticated
from rest_framework_simplejwt.backends       import TokenBackend
from authApp.models.auction import Bid,Auction
from authApp.serializers.auctionSerializer import BidSerializer,AuctionSerializer 
from rest_framework.exceptions               import PermissionDenied


class AuctionCreateview(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = AuctionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if Auction.objects.filter(product=request.data['product']).exists():
           return Response("La subasta ya existe.",  status=status.HTTP_400_BAD_REQUEST)    
        serializer.save()
        return Response("subasta fue creada exitosamente.", status=status.HTTP_201_CREATED)

class AuctionDetailView(generics.RetrieveAPIView):
        serializer_class   = AuctionSerializer 
        queryset           = Auction.objects.all()
        def get(self, request, *args, **kwargs):
            
            return super().get(request, *args, **kwargs)

class AuctionListView (generics.ListAPIView):
        serializer_class   = AuctionSerializer
        def get_queryset(self):
            queryset = Auction.objects.all()
            return queryset 

class AuctionUpdateView(generics.UpdateAPIView):
        serializer_class   =  AuctionSerializer
        queryset           =  Auction.objects.all()
        def put(self, request, *args, **kwargs):
            super().update(request, *args, **kwargs)  
            return Response(f"Se actualizó la subasta",status=status.HTTP_200_OK)   
 
class  AuctionDeleteView(generics.DestroyAPIView):
        serializer_class   =  AuctionSerializer
        queryset            = Auction.objects.all()
        def delete(self, request, *args, **kwargs):

            super().destroy(request, *args, **kwargs)
            return Response(f"Se eliminó la subasta",status=status.HTTP_200_OK)
    
 
    