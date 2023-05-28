from services import newsapi, youtube
import feedgenerator
import datetime


def generate_feed(keyword: str):
    # 抓出新聞與影片
    resp_news = newsapi.search(keyword)
    resp_youtube = youtube.search_youtube_video(keyword)

    feed = feedgenerator.Rss201rev2Feed(
        title='News Feed',
        description='A feed of news',
        language='en',
        link=""
    )

    # 依序跑迴圈產生 feed item
    for newElement in resp_news:
        feed.add_item(
            title=newElement['title'],
            link=newElement['url'],
            description="<![CDATA[ %s ]]>" % newElement['content'],
            pubdate=datetime.datetime.fromisoformat(newElement["publishedtime"][:-1]), # 將 'Z' 刪除後再解析為日期時間物件
        )

    for videoElement in resp_youtube:
        feed.add_item(
            title=videoElement['video_title'],
            link=videoElement['video_url'],
            description="<![CDATA[ %s ]]>" % videoElement['video_summary'],
            pubdate=datetime.datetime.fromisoformat(videoElement["video_publish_time"][:-1]),
        )

    return feed.writeString('utf-8')
