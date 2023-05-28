# 呼叫 newsapi 並傳回搜尋結果
# 第一個參數會是 newsapi 所需要的 apikey
# 第二個參數則是要搜尋的關鍵字

#'title': 新聞標題 , 
#'content': 新聞摘要 ,
#'url': 網址 , 
#'publishedtime': 發布時間 

import requests
import json
import os

apikey = os.getenv("NEWSAPI_KEY")
apibaseurl = 'https://newsapi.org/v2/'
#設定起始日期
# date_start = '2022-01-01'
#設定結束日期
# date_end = '2023-03-30'

#搜尋頭條新聞
def search_top(keyword):
    url = apibaseurl + 'top-headlines'
    params = {'q': keyword, 
            'pageSize': 20,
            'apiKey': apikey,
            'country': 'tw' }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        json_response = json.loads(response.text)
        news_lists = []
        # print(len(json_response['articles']))
        for article in json_response['articles']:
            news = {
                'title': article['title'],
                'content': article['content'],
                'url': article['url'],
                'publishedtime': article['publishedAt'],
            }
            news_lists.append(news)
        return news_lists
    else:
        return None    

#搜尋所有新聞
def search(keyword):
    url = apibaseurl + 'everything'
    params = {'q': keyword, 
              'pageSize': 20,  #分頁設定傳回20筆資料, 
              'page': 1,       #傳回第一頁的資料
              'sortBy': 'publishedAt', #以發布時間排序
              'apiKey': apikey}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        json_response = json.loads(response.text)
        news_lists = []
        print(len(json_response['articles']))
        for article in json_response['articles']:
            news = {
                'title': article['title'],
                'content': article['content'],
                'url': article['url'],
                'publishedtime': article['publishedAt'],
            }
            news_lists.append(news)
        return news_lists
    else:
        return None

if __name__ == '__main__':
    result = search('國民黨')
    # print(result)