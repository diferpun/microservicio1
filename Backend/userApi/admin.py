from django.contrib                 import admin
from .models.user                   import User
from .models.auctionModels          import Bid
from .models.auctionModels          import Auction

# Register your models here.
admin.site.register(User)
admin.site.register(Bid)
admin.site.register(Auction)

 