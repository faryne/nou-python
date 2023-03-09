# 引入 Flask
from flask import Flask

# 引入路由列表：每一條路由都代表一個操作
from controllers import index

# 初始化 Flask App：這裡使用基礎設定
app = Flask(__name__)

# 開始註冊路由
app.add_url_rule("/", None, index.hello)    # [GET] 首頁


# 當執行 python3 app.py 時才會滿足條件，並執行 if 內的程式碼
# 也就是讓 Flask 跑在 3000 這個 port 號上
# 否則預設跑在 5000 這個 port 號
if __name__ == "__main__":
    app.run(port=3000)
