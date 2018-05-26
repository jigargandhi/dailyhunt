from django.shortcuts import render
from django.views.generic import View
from .forms import VideoForm


class AddVideoView(View):
    def post(self, request):
        pass

    def get(self, request):
        videoForm = VideoForm()
        return render(request, 'buzz\create_video.html', {'form': videoForm})
