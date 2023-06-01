# 呼叫 youtube api 並傳回搜尋結果
# 第一個參數會是要搜尋的關鍵字


import argparse
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import os

# 設定 API 金鑰
DEVELOPER_KEY = os.getenv("YOUTUBE_APIKEY")

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

        results = []
        # 取出所有搜尋結果的影片標題、ID、描述、URL 及發佈時間並印出
        for search_result in search_response.get('items', []):
            if search_result['id']['kind'] == 'youtube#video':
                video_title = search_result['snippet']['title']
                video_summary = search_result['snippet']['description']
                video_url = f"https://www.youtube.com/watch?v={search_result['id']['videoId']}"
                video_publish_time = search_result['snippet']['publishedAt']
                video_id = search_result['id']['videoId']

                results.append({
                    'video_title': video_title,
                    'video_summary': video_summary,
                    'video_url': video_url,
                    'video_publish_time': video_publish_time,
                    'video_id': video_id
                })
        
        # 回傳取得的資料
        return results
    except HttpError as e:
        # 拋出 HttpError 錯誤供呼叫端處理
        raise e
