from typing import ClassVar
from django.conf                             import settings
from django.http.response import Http404
from rest_framework                          import serializers, status, views
from rest_framework.response                 import Response
from rest_framework_simplejwt.serializers    import TokenObtainPairSerializer
from authApp.serializers.userSerializer import UserSerializer
from rest_framework  import generics, status
from rest_framework.permissions import IsAuthenticated
from authApp.models.user import User

 
class UserCreateView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        tokenData = {"username":request.data["username"],
                    "password":request.data["password"]}
        tokenSerializer = TokenObtainPairSerializer(data=tokenData)
        tokenSerializer.is_valid(raise_exception=True)
        return Response(tokenSerializer.validated_data, status=status.HTTP_201_CREATED)
    

class UserDetailView(views.APIView):
    def get_user(self, id):
        try:
            return User.objects.get(pk=id)
        except User.DoesNotExist:
            raise Http404
    def get(self, request, *args, **kwargs):
        user= self.get_user(kwargs['pk'])
        print(user)
        user_serializer = UserSerializer(user)
        return Response(user_serializer.data, status=status.HTTP_200_OK)

class UsersView(views.APIView):
      
      def get(self, request, *args, **kwargs):
    
        users=User.objects.all()
        users_serializers = UserSerializer(users, many=True)
        return Response(users_serializers.data,status=status.HTTP_200_OK)

class UserUpdateView(views.APIView):
      def get_user(self, id):
        try:
            return User.objects.get(pk=id)
        except User.DoesNotExist:
            raise Http404
      
      def put(self, request, *args, **kwargs):
        
        user = self.get_user(kwargs['pk'])
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(f"Se actualizó el usuario con el ID # {kwargs['pk']} ", status=status.HTTP_200_OK)

        return Response("No se pudo actualizar el usuario.")

class UserDeleteView(views.APIView):
    def get_user(self, id):
        try:
            return User.objects.get(pk=id)
        except User.DoesNotExist:
            raise Http404
    
    
    def delete(self, request, *args, **kwargs):
        user= self.get_user(kwargs['pk'])
        user_serializer = UserSerializer(user)
        user.delete()
        return Response(f"Se ha eliminado el usuario con el ID # {kwargs['pk']} ", status=status.HTTP_200_OK)