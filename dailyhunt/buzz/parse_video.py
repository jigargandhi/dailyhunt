from urllib.parse import urlparse
from urllib.request import urlopen
import request
from bs4 import BeautifulSoup

def get_video_info(video_url):
    parsed = urlparse(video_url)
    if parsed.netloc.index("youtube") >=0 or parsed.netloc.index("youtu.be")>=0:
        return get_youtube_info(video_url)
    else:
        return get_other_info(video_url)

def get_youtube_info(video_url):
    """
    Gets the embed info from youtube using https://www.youtube.com/oembed?url={VIDEO_URL}&format=json 
    """
    info_url = " https://www.youtube.com/oembed?url={}&format=json".format(video_url)
    with urlopen(info_url) as response:
        json_data= response.data()
    
    pass
    

def get_other_info(video_url):
    pass
