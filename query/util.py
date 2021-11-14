import requests
import time
from . import models, secret
from datetime import datetime

def save_data(q, results, task_id):
    for result in results:
        video_data = models.Data(
            _id = task_id,
            query = q,
            title = result['snippet']['title'],
            des = result['snippet']['description'],
            date = datetime.fromisoformat(result['snippet']['publishedAt'][:-1]),
            url = f'https://www.youtube.com/watch?v={ result["id"] }',
            thumb = result['snippet']['thumbnails']['high']['url']
        )
        video_data.save()

def query(q = 'football', task_id=None):
    search_url = 'https://www.googleapis.com/youtube/v3/search'

    search_params = {
        'part' : 'snippet',
        'q' : q,
        'key' : secret.YOUTUBE_DATA_API_KEY,
        'maxResults' : 50,
        'type' : 'video'
    }
    
    r = requests.get(search_url, params=search_params)
    results = r.json()['items']
    nextPageToken = r.json()['nextPageToken']
    save_data(q, results, task_id)
    for n in (1, 9):
        search_params = {
        'part' : 'snippet',
        'q' : q,
        'key' : secret.YOUTUBE_DATA_API_KEY,
        'maxResults' : 50,
        'type' : 'video',
        'pageToken' : nextPageToken
        }
        r = requests.get(search_url, params=search_params)
        nextPageToken = r.json()['nextPageToken']
        results = r.json()['items']
        save_data(q, results, task_id)
    print("Completed query")

def repeated_calls(q, task_id):
    for num in (360):
        query(q, task_id)
        time.sleep(10)

def retrive(task_id, page):
    vid = models.Data.objects.filter(_id=task_id).order_by('-date')[10 * (page - 1) : 10 * page]
    vid = [str(vi)for vi in vid]
    return ({"response":list(vid)})