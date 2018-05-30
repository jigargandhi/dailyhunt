from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
# Create your views here.
from .models import News, Language,Tags
from .forms import NewsForm, TagForm



class NewNewsView(View):
    def post(self, request):
        form = NewsForm(request.POST)
        if form.is_valid():
            news = form.save(commit=False)
            news.save()
            return redirect('home')
        return render(request, 'news/create_news.html', {'form': form})

    def get(self, request):
        form = NewsForm()
        return render(request, 'news/create_news.html', {'form': form})


class NewsView(View):
    def get(self, request, news_id=None,slug_part=None):
        if news_id is not None:
            news = get_object_or_404(News, pk=news_id)
            return render(request, 'see_article.html', {'news': news})
        else:
            news = News.objects.all()
            tags= Tags.objects.all()
            return render(request, 'news/browse_news.html', {'news': news,'tags':tags})


class TagsView(View):
    def post(self, request):
        form = TagForm(request.POST)
        if form.is_valid():
            tag = form.save(commit=False)
            tag.save()
            return redirect('home')
        else:
            form = TagForm()
        return render(request, 'create_tag.html',{'form':form})
        
    def get(self, request):
        form = TagForm()
        return render(request, 'create_tag.html',{'form':form})

