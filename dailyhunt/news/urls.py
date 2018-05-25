from django.urls import include, path
from news import views


urlpatterns = [
    path('', views.index, name='home'),
    path('create', views.NewNewsView.as_view(), name='create_news'),
    path('browse', views.NewsView.as_view(), name='browse'),
    path('browse/<int:news_id>', views.NewsView.as_view(), name='browse'),
    path('create_tag', views.TagsView.as_view(), name='create_tag')
]
