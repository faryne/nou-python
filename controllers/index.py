import flask
from services import youtube, newsapi


# 首頁：顯示查詢輸入框
def hello():
    return flask.render_template("index.html")


# rss 頁面：傳入 keyword 據此從 newsapi 和 youtube 取出相關資料並產生給 RSS 閱讀器的內容
def rss(keyword: str):
    resp_youtube = youtube.search("", keyword)
    resp_newsapi = newsapi.search("", keyword)
    return flask.render_template("rss.xml",
                                 youtube=resp_youtube,
                                 newsapi=resp_newsapi)


# html 頁面：傳入 keyword 據此從 newsapi 和 youtube 取出相關資料並產生給瀏覽器看的 HTML 內容
def topic(keyword: str):
    resp_youtube = youtube.search("", keyword)
    resp_newsapi = newsapi.search("", keyword)
    return flask.render_template("topic.html",
                                 youtube=resp_youtube,
                                 newsapi=resp_newsapi)