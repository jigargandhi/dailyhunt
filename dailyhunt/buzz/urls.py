from django.urls import include, path
from .views import AddVideoView, VideosView

app_name='buzz'
urlpatterns=[
    path('create',AddVideoView.as_view(),name='create'),
    path('browse/',VideosView.as_view(),name='browse'),
    path('browse/<int:video_id>',VideosView.as_view(),name='see')
]