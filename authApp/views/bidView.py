from typing import ClassVar
from django.conf                             import settings
from rest_framework                          import status, views
from rest_framework.response                 import Response
from rest_framework_simplejwt.serializers    import TokenObtainPairSerializer
from authApp.serializers.userSerializer      import UserSerializer
from rest_framework                          import generics, status
from rest_framework.permissions              import IsAuthenticated
from rest_framework_simplejwt.backends       import TokenBackend
from authApp.models.auction import Bid,Auction
from authApp.serializers.auctionSerializer  import BidSerializer,AuctionSerializer 
from rest_framework.exceptions               import PermissionDenied
from django.utils import timezone 
import datetime                        

class BidCreateView(views.APIView):   
     
    def post(self, request, *args, **kwargs):
        serializer = BidSerializer(data=request.data)
        serializer.is_valid()
        auction=Auction.objects.get(auction_id=request.data['auction'])
        current_offer=auction.base_offer
        
        bid_date=datetime.datetime.now(tz=timezone.utc)
       
        if  float(request.data['offer']) <= float(current_offer):
            return Response("valor de puja bajo.") 
        
        if  bid_date>auction.time_ending:
            return Response("La subasta expiró.") 
        
        auction.base_offer=request.data['offer']
        serializer.save()
        auction.save()
        return Response("Se creó la puja.", status=status.HTTP_201_CREATED)

class BidDetailView(views.APIView):
    
    def get(self, request, *args, **kwargs):
        
        bids = Bid.objects.filter(user_id=kwargs["user"])
        bids_serializers = BidSerializer(bids, many=True)
        return Response(bids_serializers.data)

class BidsView(views.APIView):
      
      def get(self, request, *args, **kwargs):
    
        bids=Bid.objects.all()
        bids_serializers = BidSerializer(bids, many=True)
        return Response(bids_serializers.data, status=status.HTTP_202_ACCEPTED)
    
class BidTopView(views.APIView):
      
      def get(self, request, *args, **kwargs):
    
        bids=Bid.objects.filter(user_id=self.kwargs["user"], auction_id=self.kwargs["auction"]).order_by('-offer')
        bids_serializers = BidSerializer(bids, many=True)
        return Response(bids_serializers.data, status=status.HTTP_202_ACCEPTED)

class BidDeleteView(generics.DestroyAPIView):

        
        def delete(self, request, *args, **kwargs):
            
            auctions = kwargs['auction']
            users= kwargs['user']
            self.queryset = Bid.objects.filter(user_id=self.kwargs["user"],auction_id=int(kwargs['auction']))
            
            if  not self.queryset.exists():
                return Response("No existe la puja. ")

            self.queryset.delete() 
            return Response(f"Se eliminaron las pujas correspondientes a la subasta {auctions} del cliente {users}",status=status.HTTP_200_OK) 