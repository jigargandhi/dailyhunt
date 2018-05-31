from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from .forms import VideoForm
from .parse_video import get_video_info
from .models import Video
from news.models import Tags
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
            except Exception as ex:
                metaInfo = None
                return HttpResponseBadRequest("unable to find the content at the url because "+str(ex))

    def get(self, request):
        videoForm = VideoForm()
        return render(request, 'buzz\create_video.html', {'form': videoForm})


class VideosView(View):
    def get(self, request, video_id=None):
        if video_id is not None:
            video = get_object_or_404(Video, pk=video_id)
            return render(request, 'buzz/see_video.html', {'video': video})
        else:
            videos = Video.objects.all()
            tags= Tags.objects.all()
            return render(request, 'buzz/browse_videos.html', {'videos': videos,'tags':tags})