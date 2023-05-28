import flask
from flask import request

from services import youtube, newsapi, rss_feed

default_keyword = "台中捷運"

# 首頁：顯示查詢輸入框
def hello():
    keyword = request.args.get("keyword", default_keyword)
    resp_youtube = youtube.search_youtube_video(keyword)
    resp_newsapi = newsapi.search(keyword)
    return flask.render_template("index.html",
                                 videos=resp_youtube,
                                 news=resp_newsapi)


# rss 頁面：傳入 keyword 據此從 newsapi 和 youtube 取出相關資料並產生給 RSS 閱讀器的內容
def rss():
    keyword = request.args.get("keyword", default_keyword)
    resp = rss_feed.generate_feed(keyword)
    return flask.Response(flask.render_template("rss.xml", resp=resp), mimetype="application/xml")


# html 頁面：傳入 keyword 據此從 newsapi 和 youtube 取出相關資料並產生給瀏覽器看的 HTML 內容
def topic():
    keyword = request.args.get("keyword", default_keyword)
    resp_youtube = youtube.search_youtube_video(keyword)
    resp_newsapi = newsapi.search(keyword)
    return flask.render_template("topic.html",
                                 keyword=keyword,
                                 videos=resp_youtube,
                                 news=resp_newsapi)