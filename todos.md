## 專案目標
1. 串接 newsapi.org 所提供的文字新聞或是 Youtube 提供的影音
2. 在瀏覽器上即可瀏覽內容
3. 在 RSS 閱讀器也可以瀏覽訂閱的主題

目前已經先把基底部署一份至：https://nou-python.maid.tw

## 使用技術
* Python 3.x 
* Flask 網站開發框架
* 網站放置在 Google Cloud Platform 的 Cloud Run 服務上執行

## 組員名單及工作分配
| 姓名     | email                | 工作分配                                    |
|--------|----------------------|-----------------------------------------|
| *I 組 Python 奇妙之旅* |                             | 
| 謝育典    | faryne@faryne.tw     | Flask 架構設定及自動化部署<br/>首頁頁面和公版編排<br/>口頭報告 | 
| 陳柏聿    | dichotomania@gmail.com | newsapi.org API 串接                      |
| 楊函倞    | hanjingus8@gmail.com | YouTube API 串接                          |
| 姜惠敏    | djiang.nou@gmail.com |                                         |
| 李卉榆    | evalee426@gmail.com  |                                         |
| 黃意恩    | w2910222@gmail.com   |                                         |

## 須完成項目
---
* [x] Flask 架構設定及自動化部署
* [ ] 串接 `newsapi api` 的主程式碼
  * [x] newsapi 的 apikey 提供(參閱討論版)
  * [ ] 主程式碼撰寫
* [ ] 串接 `youtube api` 的主程式碼
  * [x] youtube 的 apikey 提供(參閱討論版)
  * [ ] 主程式碼撰寫
* [ ] 建立首頁頁面
* [ ] 整合以上 API 結果並產生出顯示頁面
* [ ] 整合以上 API 結果並產生出 RSS Feeds
* [ ] 整理成文字報告或簡報
* [ ] 口頭報告