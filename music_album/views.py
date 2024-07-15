from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from rest_framework.views import APIView

from rest_framework.generics import RetrieveUpdateDestroyAPIView ,CreateAPIView

from rest_framework.response import Response

from rest_framework.decorators import action

from music_album.serializers import AlbumSerializer,TrackSerializer,ReviewSerializer,UserSerializer

from music_album.models import Album,Tracks,Review

from music_album.permissions import OwnerOnly

from rest_framework import authentication,permissions 



class UserView(APIView):

    def post(self,request,*args,**kwargs):

        serializer=UserSerializer(data=request.data)
        
        if serializer.is_valid():

            serializer.save()

        return Response(data=serializer.data) 

class AlbumViewSetView(ModelViewSet):

    serializer_class=AlbumSerializer

    queryset=Album.objects.all()

    authentication_classes=[authentication.TokenAuthentication]

    permission_classes=[permissions.IsAdminUser]


    @action(methods=['post'],detail=True)
    def add_track(self,request,*args,**kwargs):

        id=kwargs.get('pk')

        album_instance=Album.objects.get(id=id)

        serializer=TrackSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save(album=album_instance)

            return Response(data=serializer.data)

        else:
            
            return Response(data=serializer.errors)

    
        
class TrackViewSetView(RetrieveUpdateDestroyAPIView):

    serializer_class=TrackSerializer

    queryset=Tracks.objects.all()

    authentication_classes=[authentication.TokenAuthentication]

    permission_classes=[permissions.IsAdminUser]


class AddReviewView(APIView):

    authentication_classes=[authentication.TokenAuthentication]

    permission_classes=[OwnerOnly]

       
    def post(self,request,*args,**kwargs):

        id=kwargs.get('pk')

        album_instance=Album.objects.get(id=id)

        serializer=ReviewSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save(user=request.user,album=album_instance)

            return Response(data=serializer.data)
        
        else:

            return Response(data=serializer.errors)
   

class ReviewViewSetView(RetrieveUpdateDestroyAPIView):

    serializer_class=ReviewSerializer

    queryset=Review.objects.all()

    authentication_classes=[authentication.TokenAuthentication]

    permission_classes=[OwnerOnly]
    
    
