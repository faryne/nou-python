
from flask import Flask, Response
import feedgenerator
from googleapiclient.discovery import build
import datetime

app = Flask(__name__)

# YouTube Data API設置
api_key = "AIzaSyCmr2tULsG6dtLI1cbtoyWihfe9yPW4be4"
youtube = build('youtube', 'v3', developerKey=api_key)

# 影片資料
videos = []

def generate_rss_feed():
    feed = feedgenerator.Rss201rev2Feed(
        title='YouTube Videos',
        link='http://127.0.0.1:5000/',
        description='A feed of YouTube videos',
        language='en'
    )

    for video in videos:
        pubdate = datetime.datetime.strptime(video['publishedAt'], "%Y-%m-%dT%H:%M:%SZ")

        feed.add_item(
            title=video['title'],
            link=f"https://www.youtube.com/watch?v={video['videoId']}",
            description=video['description'],
            pubdate=pubdate,
        )

    rss = feed.writeString('utf-8')

    return rss

@app.route('/')
def rss_feed():
    rss = generate_rss_feed()
    return Response(rss, mimetype='text/xml')

@app.route('/search_videos/<q>')
def search_videos(q):
    global videos
    search_response = youtube.search().list(
        q=q,
        type='video',
        part='id,snippet',
        maxResults=10
    ).execute()

    videos = []
    for search_result in search_response.get('items', []):
        video = {
            'title': search_result['snippet']['title'],
            'videoId': search_result['id']['videoId'],
            'description': search_result['snippet']['description'],
            'publishedAt': search_result['snippet']['publishedAt']
        }
        videos.append(video)

    rss = generate_rss_feed()
    return Response(rss, mimetype='text/xml')

if __name__ == '__main__':
    app.run(debug=True, port=5000)


rss_video_result = search_videos("台中捷運")