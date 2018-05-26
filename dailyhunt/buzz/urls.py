from django.urls import include, path
from .views import AddVideoView

urlpatterns=[
    path('create',AddVideoView.as_view(),name='create')
]