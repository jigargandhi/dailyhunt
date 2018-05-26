from django.urls import include, path
from news import views


urlpatterns = [
    path('create', views.NewNewsView.as_view(), name='create'),
    path('browse', views.NewsView.as_view(), name='browse'),
    path('browse/<int:news_id>', views.NewsView.as_view(), name='browse'),
    path('create_tag', views.TagsView.as_view(), name='create_tag')
]
