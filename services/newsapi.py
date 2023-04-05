# 呼叫 newsapi 並傳回搜尋結果
# 第一個參數會是 newsapi 所需要的 apikey
# 第二個參數則是要搜尋的關鍵字

import requests
import json

apikey = 'ab9b50bfa2164561974d16942e1b86a7'

#設定起始日期
# date_start = '2022-01-01'
#設定結束日期
# date_end = '2023-03-30'

#搜尋頭條新聞
def search_top(apikey: str, keyword: str):
    url = 'https://newsapi.org/v2/top-headlines'
    params = {'q': keyword, 'apiKey': apikey, 'country': 'tw' }
    response = requests.get(url, params=params)
    return json.loads(response.text)

#搜尋所有新聞
def search(apikey: str, keyword: str):
    url = 'https://newsapi.org/v2/everything'
    params = {'q': keyword, 'apiKey': apikey}
    response = requests.get(url, params=params)
    return json.loads(response.text)

result = search(apikey, '星宇航空')

#回傳狀態
print(result['status'])

#總共有幾則新聞
print(result['totalResults'])

#articles文章陣列  
for article in result['articles']:
    #來源
    print(article['source']['name'])
    #作者
    print(article['author'])
    #標題
    print(article['title'])
    #內容
    print(article['content'])
    #網址
    print(article['url'])
    #圖片
    print(article['urlToImage'])
    #發布時間
    print(article['publishedAt'])
    #來源
    print(article['source']['name'])
    print('-----------------------')

