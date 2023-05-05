
from flask import Flask, Response
import feedgenerator
import datetime

app = Flask(__name__)

# 新聞資料
news = [{'title': '台湾カリスマ経営者の政界リベンジが起こす波乱 強すぎる親中イメージ､公認の獲得は難しい | 中国･台湾 | 東洋経済オンライン', 'content': 'Copyright©Toyo Keizai Inc.All Rights Reserved.', 'url': 'https://toyokeizai.net/articles/-/664753', 'publishedtime': '2023-04-06T22:00:00Z'},
        {'title': '#最新看TVBS【LIVE】郭台銘東海大學演講會前聯合訪問 - TVBS NEWS', 'content': 'We use cookies and data to<ul><li>Deliver and maintain Google services</li><li>Track outages and protect against spam, fraud, and abuse</li><li>Measure audience engagement and site statistics to unde… [+1131 chars]', 'url': 'https://consent.google.com/ml?continue=https://news.google.com/rss/articles/CCAiCzJaTDlpZHY2VXg0mAEB?oc%3D5&gl=FR&hl=en-US&cm=2&pc=n&src=1', 'publishedtime': '2023-04-27T04:11:11Z'}]

# 轉換為 RSS XML 格式
@app.route('/')
def rss_feed():
    feed = feedgenerator.Rss201rev2Feed(
        title='News Feed',
        link='http://127.0.0.1:5000/',
        description='A feed of news',
        language='en'
    )

    for item in news:
        # 將 'Z' 刪除後再解析為日期時間物件
        pubdate = datetime.datetime.fromisoformat(item['publishedtime'][:-1])

        feed.add_item(
            title=item['title'],
            link=item['url'],
            description=item['content'],
            pubdate=pubdate,
        )

    rss = feed.writeString('utf-8')

    return Response(rss, mimetype='text/xml')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
