# 引入 Flask
import os.path

import dotenv
from flask import Flask

# 載入 env 環境變數設定檔案的套件
import dotenv


# 引入路由列表：每一條路由都代表一個操作
from controllers import index

# 初始化 Flask App：這裡使用基礎設定
app = Flask(__name__)

# 檢查是否有 .env 檔。本機開發測試用需要有這個檔案，不然就需要在系統環境中加入 .env.example 中的所需要的兩個環境變數
# 也可以將在本專案內的 .env.example 複製一份變成 .env 並填入 newsapi 和 youtube 所使用的 apikey
if os.path.exists(".env"):
    dotenv.load_dotenv(".env")

# 開始註冊路由
app.add_url_rule("/", None, index.hello)                        # [GET] 首頁
app.add_url_rule("/topic", None, index.topic)                   # [GET] 主題頁
app.add_url_rule("/rss", None, index.rss)                       # [GET] 主題頁的 RSS 版本


# 當執行 python3 app.py 時才會滿足條件，並執行 if 內的程式碼
# 也就是讓 Flask 跑在 3000 這個 port 號上
# 否則預設跑在 5000 這個 port 號
if __name__ == "__main__":
    app.run(port=3000)
