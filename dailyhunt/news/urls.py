from django.urls import include, path
from news import views

app_name='news'
urlpatterns = [
    path('create/', views.NewNewsView.as_view(), name='create'),
    path('browse/', views.NewsView.as_view(), name='browse'),
    path('browse/<int:news_id>/<slug:slug_part>/', views.NewsView.as_view(), name='see'),
    path('create_tag/', views.TagsView.as_view(), name='create_tag')
]
