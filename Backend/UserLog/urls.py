"""UserLog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from userApi                        import views
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView) 
from django.urls                    import path

urlpatterns = [
    #path('admin/', admin.site.urls),
    #path('login/',TokenObtainPairView.as_view()),
    path('login/',views.MyTokenObtainPairView.as_view()),
    path('refresh/',TokenRefreshView.as_view),
    #path('verifyToken/', views.VerifyTokenView.as_view()),
    path('createuser/',views.userViews.UserCreateView.as_view()),
    path('user/<int:pk>',views.userViews.UserDetailView.as_view()),
    path("updateuser/<int:pk>", views.userViews.UserUpdateView.as_view()),
    
    path("createauction/", views.auctionViews.AuctionCreateview.as_view()),
    path("auctiondetailView/<int:pk>", views.auctionViews.AuctionDetailView.as_view()),
    path("auctionupdateView/<int:pk>", views.auctionViews.AuctionUpdateView.as_view()),
    path("auctiondeleteView/<int:pk>", views.auctionViews.AuctionDeleteView.as_view()),
    path("auctionlistview/", views.auctionViews.AuctionListView.as_view()),
    
    path("createbid/", views.bidViews.BidCreateview.as_view()),
    path("detailbid/<int:user>", views.bidViews.BidDetailView.as_view()),
    path("topbid/<int:user>/<int:auction>", views.bidViews.BidTopView.as_view()),
    path("deletebid/<int:auction>",views.bidViews.BidDeleteview.as_view())
]
