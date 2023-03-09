import flask


# 首頁
def hello():
    return flask.render_template("index.html")
