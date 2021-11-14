# YoutubeAPIQuery
The repo uses Django, Celery and Docker to run search query using Youtube API and maintains database of videos of lastest video for 10 min asynchronously. And GET api can be used to show paginated response from the database.


#How to use and test the repo

Clone into your system run command `sudo docker-compose up -d --build` to start the server 

API to a search for youtube videos
```
curl --location --request POST 'localhost:1337/search/' \
--header 'Content-Type: text/plain' \
--data-raw '{
    "q": "football"
}'
```

API to see the result using the task_id recieved in previous API
```
curl --location --request GET 'localhost:1337/search/<task_id>
```

API to see next pages in response. (the API support maximum of 50 pages of data)

```
curl --location --request GET 'localhost:1337/search/<task_id>/<page>
```

