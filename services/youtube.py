# 呼叫 youtube api 並傳回搜尋結果
# 第一個參數會是 youtube 所需要的 apikey
# 第二個參數則是要搜尋的關鍵字


import argparse
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# 設定 API 金鑰
DEVELOPER_KEY = 'AIzaSyAb2woptImKjZ505eIujPQLQh8lzb7qchg'

def search_youtube_video(search_keyword):
    # 建立 YouTube API 服務物件
    youtube = build('youtube', 'v3', developerKey=DEVELOPER_KEY)

    try:
        # 使用 search() 方法搜尋影片
        search_response = youtube.search().list(
            q=search_keyword, # 搜尋關鍵字
            type='video', # 搜尋類型為影片
            part='id,snippet', # 回傳資訊包含影片 ID 及標題等基本資訊
            maxResults=10 # 回傳搜尋結果數量
        ).execute()

        # 取出所有搜尋結果的影片標題及 ID 並印出
        for search_result in search_response.get('items', []):
            if search_result['id']['kind'] == 'youtube#video':
                print('{} ({})'.format(search_result['snippet']['title'], 
                                       search_result['id']['videoId']))

        # 回傳取得的資料
        return [{...}, {...}]
    except HttpError as e:
        # 拋出 HttpError 錯誤供呼叫端處理
        raise e
    finally:
        # 回傳空陣列
        return []

