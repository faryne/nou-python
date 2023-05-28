## 如何啟動
以下操作請使用 Windows 下的終端機或是 macOS 的 Terminal 執行

1. 請確保機器環境有 `python3`、`pip` 與 `git` 等項目。
2. 打開終端機，執行以下指令：`git clone https://github.com/faryne/nou-python.git`
3. 接著切換到目錄內。如果沒做什麼操作的話，應該只要下 `cd nou-python` 即可。
4. 執行 `python3 -m venv .venv` 以建立一個虛擬環境，所有專案所需的東西會以這個虛擬環境中為主而不會去看系統的。之後安裝的套件也是安裝到該目錄。
5. 執行 `.venv/Scripts/activate.bat` 啟用虛擬環境
6. 將 `.env.example` 複製為 .env ，並將 `NEWSAPI_KEY` 及 `YOUTUBE_APIKEY` 分別填入 `newsapi.org` 以及 `Youtube` 的 apikey
7. 執行以下指令安裝所需要的 python 套件：`python3 -m pip install -r requirements.txt`
8. 執行以下指令：`python3 -m flask run`，然後打開瀏覽器輸入 `http://localhost:5000` 即可。

## 目錄說明
### `controllers`
放置各種路由操作 function 

### `services`
放置各種操作，例如呼叫 API 等檔案的地方。

### `templates`
放置模板、視圖檔案的地方。

## 工作分配
[請參考](./todos.md)

## 參考資源
* [Flask 教學文件](https://dormousehole.readthedocs.io/en/latest/)
* [專案網址](https://nou-python.maid.tw)

