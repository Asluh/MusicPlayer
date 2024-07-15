from rest_framework import serializers

from django.contrib.auth.models import User

from music_album.models import Album,Tracks,Review


class UserSerializer(serializers.ModelSerializer):

    class Meta:

        model=User

        fields=['username','password','email']

    def create(self, validated_data):
        
        return User.objects.create_user(**validated_data)


class TrackSerializer(serializers.ModelSerializer):
    
    album=serializers.StringRelatedField(read_only=True)

    class Meta:

        model=Tracks

        fields="__all__"

        read_only_fields=['id','album']

class ReviewSerializer(serializers.ModelSerializer):

    album=serializers.StringRelatedField(read_only=True)

    class Meta:

        model=Review

        fields="__all__"

        read_only_fields=['id','created_date','album','user']


class AlbumSerializer(serializers.ModelSerializer):

    tracks=TrackSerializer(many=True,read_only=True)
    
    reviews=ReviewSerializer(many=True,read_only=True)
 
    class Meta:

        model=Album

        fields="__all__"

        read_only_fields=['id','created_date','updated_date','is_active']


