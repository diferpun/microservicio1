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
from django.utils                            import timezone
import datetime                        

class BidCreateview(views.APIView):   
    permission_classes = (IsAuthenticated,) 
    def post(self, request, *args, **kwargs):
        serializer = BidSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token        = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data   = tokenBackend.decode(token,verify=False)
        #aux=Bid.objects.filter(auction_id=request.data['auction'],user_id=request.data['user']).exists()         
        #print("check ################",aux)
        #################### arreglar esto ######################################
        auction=Auction.objects.get(auction_id=request.data['auction'])
        current_offer=auction.base_offer
        bid_date=datetime.datetime.now(tz=timezone.utc)
        
        if request.data['user'] != valid_data['user_id']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED) 
        # print("######",type(request.data['offer']),type(current_offer))
        # print("######",float(request.data['offer']) <= float(current_offer))
       
        if  float(request.data['offer']) <= float(current_offer):
            stringResponse = {'detail':'low bid'}
            return Response(stringResponse, status=status.HTTP_400_BAD_REQUEST) 
        
        if  bid_date>auction.time_ending:
            stringResponse = {'detail':'auction expired'}
            return Response(stringResponse, status=status.HTTP_400_BAD_REQUEST) 
        
        auction.base_offer=request.data['offer']
        serializer.save()
        auction.save()
        return Response(request.data, status=status.HTTP_201_CREATED)

class BidDetailView(generics.ListAPIView):
    serializer_class   = BidSerializer
    permission_classes = (IsAuthenticated,)
    def get_queryset(self):
        token        = self.request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data   = tokenBackend.decode(token,verify=False)
        #print("hola 1",valid_data['user_id'])
        #print("hola 4",self.kwargs["user"])
        if valid_data['user_id'] != self.kwargs['user']:
            print("son diferentes")  
            #stringResponse = {'detail':'Unauthorized Request'}
            #return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
            raise PermissionDenied()
        
        queryset = Bid.objects.filter(user_id=self.kwargs["user"])
        return queryset
    
class BidTopView(generics.ListAPIView):
      serializer_class   = BidSerializer
      permission_classes = (IsAuthenticated,)
      def get_queryset(self):
        token        = self.request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data   = tokenBackend.decode(token,verify=False)
        
        if valid_data['user_id'] != self.kwargs['user']:
            print("son diferentes")  
            raise PermissionDenied()
        queryset=Bid.objects.filter(user_id=self.kwargs["user"],
                                    auction_id=self.kwargs["auction"]).order_by('-offer')
        return queryset[0:1]

class BidDeleteview(generics.DestroyAPIView):
        serializer_class    = BidSerializer
        lookup_field        = 'auction'
        permission_classes = (IsAuthenticated,)
        queryset            =  Bid.objects.all()
        
        def delete(self, request, *args, **kwargs):
            
            token         = request.META.get('HTTP_AUTHORIZATION')[7:]
            tokenBackend  = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
            valid_data    = tokenBackend.decode(token,verify=False)
            
            print("###########",request.data)
            
            # if request.data['user'] != valid_data['user_id']:
            #    stringResponse = {'detail':'Unauthorized Request'}
            #    return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED) 
             
            self.queryset = Bid.objects.filter(auction_id=int(kwargs['auction']),
                                               user_id=valid_data['user_id'])
            
            if  not self.queryset.exists():
                return Response("No existe la puja ",status=status.HTTP_204_NO_CONTENT) 
            self.queryset.delete() 
            return Response("Los registros se eliminaron",status=status.HTTP_200_OK) 
        