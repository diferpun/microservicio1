from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView
from authApp import views
urlpatterns = [
    #path('admin/', admin.site.urls),
    #path('login/',TokenObtainPairView.as_view()),
    path('login/',views.MyTokenObtainPairView.as_view()),
    path('refresh/',TokenRefreshView.as_view()),
    path('verifyToken/', views.VerifyTokenView.as_view()),
    path('createuser/',views.userView.UserCreateView.as_view()),
    path('user/<int:pk>',views.userView.UserDetailView.as_view()),
    path('users',views.userView.UsersView.as_view()),
    path("updateuser/<int:pk>", views.userView.UserUpdateView.as_view()),
    path("deleteuser/<int:pk>", views.userView.UserDeleteView.as_view()),
    
    path("createauction/", views.auctionView.AuctionCreateview.as_view()),
    path("auctiondetailView/<int:pk>", views.auctionView.AuctionDetailView.as_view()),
    path("auctionupdateView/<int:pk>", views.auctionView.AuctionUpdateView.as_view()),
    path("auctiondeleteView/<int:pk>", views.auctionView.AuctionDeleteView.as_view()),
    path("auctionlistview/", views.auctionView.AuctionListView.as_view()),
    
    path("createbid/", views.bidView.BidCreateView.as_view()),
    path("detailbid/<int:user>", views.bidView.BidDetailView.as_view()),
    path("bids", views.bidView.BidsView.as_view()),
    path("topbid/<int:user>/<int:auction>", views.bidView.BidTopView.as_view()),
    path("deletebid/<int:user>/<int:auction>",views.bidView.BidDeleteView.as_view())
]