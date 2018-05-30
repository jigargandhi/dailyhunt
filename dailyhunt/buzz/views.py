from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import VideoForm
from .parse_video import get_video_info
from .models import Video
from django.http import HttpResponseBadRequest
import logging

class AddVideoView(View):
    def post(self, request):
        form = VideoForm(request.POST)
        if form.is_valid():
            video = form.save(commit=False)
            url = video.video_url
            try:
                metaInfo = get_video_info(url)
                video.thumbnail_url = metaInfo.image_url
                video.title = metaInfo.title
                video.save()
                return redirect('home')
            except:
                metaInfo = None
                return HttpResponseBadRequest("unable to find the content at the url")

    def get(self, request):
        videoForm = VideoForm()
        return render(request, 'buzz\create_video.html', {'form': videoForm})
