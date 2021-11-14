import requests
from . import models, secret
from datetime import datetime

def save_data(results):
    for result in results:
        video_data = models.Data(
            title = result['snippet']['title'],
            des = result['snippet']['description'],
            date = datetime.fromisoformat(result['snippet']['publishedAt'][:-1]),
            url = f'https://www.youtube.com/watch?v={ result["id"] }',
            thumb = result['snippet']['thumbnails']['high']['url']
        )
        video_data.save()

def query(request):
    search_url = 'https://www.googleapis.com/youtube/v3/search'

    search_params = {
        'part' : 'snippet',
        'q' : "football",
        'key' : secret.YOUTUBE_DATA_API_KEY,
        'maxResults' : 50,
        'type' : 'video'
    }
    
    r = requests.get(search_url, params=search_params)
    results = r.json()['items']
    nextPageToken = r.json()['nextPageToken']
    save_data(results)
    for n in (1, 9):
        search_params = {
        'part' : 'snippet',
        'q' : "football",
        'key' : secret.YOUTUBE_DATA_API_KEY,
        'maxResults' : 50,
        'type' : 'video',
        'pageToken' : nextPageToken
        }
        r = requests.get(search_url, params=search_params)
        nextPageToken = r.json()['nextPageToken']
        results = r.json()['items']
        save_data(results)
    print(models.Data.objects.all())
    return ''