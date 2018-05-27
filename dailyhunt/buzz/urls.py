from django.urls import include, path
from .views import AddVideoView

app_name='buzz'
urlpatterns=[
    path('create',AddVideoView.as_view(),name='create')
]