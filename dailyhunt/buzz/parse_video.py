from urllib.parse import urlparse
from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
import json

class VideoMetaInfo():

    def __init__(self, title, url, image ):
        self.title = title
        self.url = url
        self.image_url = image
    
    def __repr__(self):
        return self.__str__()    

    def __str__(self):
        return "VideoMetaInfo(title={}, url={}, image={})".format(self.title, self.url, self.image_url)
    

def get_video_info(video_url):
    parsed = urlparse(video_url)
    try:
        if parsed.netloc.index("youtube") >=0 or parsed.netloc.index("youtu.be")>=0:
            return get_youtube_info(video_url)
    except ValueError:
        return get_other_info(video_url)

def get_youtube_info(video_url):
    """
    Gets the embed info from youtube using https://www.youtube.com/oembed?url={VIDEO_URL}&format=json 
    """
    info_url = " https://www.youtube.com/oembed?url={}&format=json".format(video_url)
    with urlopen(info_url) as response:
        json_data= response.read()
        meta_info = json.loads(json_data)

        return VideoMetaInfo(meta_info['title'],video_url, meta_info['thumbnail_url'])
    

def get_other_info(video_url):
    if video_url is None:
        video_url = 'https://vimeo.com/113707214'
    response = requests.get(video_url)
    soup = BeautifulSoup(response.text)
    title=None
    thumbnail_url=None
    for meta in soup.find_all('meta'):
        if 'property' in meta.attrs:
            if meta['property']=='og:title':
                title = meta['content']
            elif meta['property']=='og:image':
                thumbnail_url = meta['content']
            else:
                continue
    
    return VideoMetaInfo(title, video_url, thumbnail_url)
