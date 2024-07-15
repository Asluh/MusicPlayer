from django.urls import path

from rest_framework.authtoken.views import ObtainAuthToken

from rest_framework.routers import DefaultRouter

from music_album import views

router=DefaultRouter()

router.register('albums',views.AlbumViewSetView,basename='albums')


urlpatterns=[

    path('token/',ObtainAuthToken.as_view(),name='obtaintoken'),
    path('register/',views.UserView.as_view(),name='register'),
    path('track/<int:pk>/',views.TrackViewSetView.as_view(),name='tracks'),
    path('review/<int:pk>/',views.ReviewViewSetView.as_view(),name='reviews'),
    path('addreview/<int:pk>/',views.AddReviewView.as_view()),

     
]+router.urls