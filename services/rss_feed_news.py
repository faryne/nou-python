
from flask import Flask, Response
import feedgenerator
import datetime
from newsapi import NewsApiClient

app = Flask(__name__)

# Initialize NewsApiClient
# newsapi = NewsApiClient(api_key="74eda8d3d1bc4243a9c3854f1d01712e")
newsapi = NewsApiClient(api_key="20611c0ca5c742bdb5fe4facec17e522")

# 新聞資料
news = []

def generate_rss_feed():
    feed = feedgenerator.Rss201rev2Feed(
        title='News Feed',
        link='http://127.0.0.1:5000/',
        description='A feed of news',
        language='en'
    )

    for item in news:
        # 將 'Z' 刪除後再解析為日期時間物件
        pubdate = datetime.datetime.fromisoformat(item['publishedAt'][:-1])

        feed.add_item(
            title=item['title'],
            link=item['url'],
            description=item['content'],
            pubdate=pubdate,
        )

    rss = feed.writeString('utf-8')

    return rss


@app.route('/')
def rss_feed():
    rss = generate_rss_feed()
    return Response(rss, mimetype='text/xml')


@app.route('/search_news/<q>/<language>')
def search_news(q, language):
    global news
    # response = newsapi.get_everything(q="台中捷運", language='zh')
    response = newsapi.get_everything(q=q, language=language)
    news = response['articles']
    rss = generate_rss_feed()
    return Response(rss, mimetype='text/xml')


if __name__ == '__main__':
    app.run(debug=True, port=5000)

rss_result = search_news("台中捷運",'zh')
# 輸出網址 http://127.0.0.1:5000/search_news/%E5%8F%B0%E4%B8%AD%E6%8D%B7%E9%81%8B/zh
