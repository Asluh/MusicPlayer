from django.db import models

from django.contrib.auth.models import User

from django.core.validators import MinValueValidator,MaxValueValidator



class Album(models.Model):

    title=models.CharField(max_length=100)

    year=models.CharField(max_length=100)

    director=models.CharField(max_length=100)
    
    language=models.CharField(max_length=100)

    created_date=models.DateTimeField(auto_now=True)

    updated_date=models.DateTimeField(auto_now=True)

    is_active=models.BooleanField(default=True)
    
    
    @property
    def tracks(self):

        return Tracks.objects.filter(album=self)
    
    @property
    def reviews(self):

        return Review.objects.filter(album=self)

    def __str__(self):

        return self.title

class Tracks(models.Model):

    title=models.CharField(max_length=100)

    singers=models.CharField(max_length=100)

    genre=models.CharField(max_length=100)

    duration=models.CharField(max_length=100)

    track_num=models.PositiveIntegerField()
    
    album=models.ForeignKey(Album,on_delete=models.CASCADE)

    def __str__(self):
        
        return self.title
    
class Review(models.Model):

    comment=models.CharField(max_length=200)

    rating=models.FloatField(validators=[MinValueValidator(1),
                                         MaxValueValidator(5)])
    
    created_date=models.DateTimeField(auto_now=True)

    album=models.ForeignKey(Album,on_delete=models.CASCADE)

    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):

        return self.comment

