# 呼叫 newsapi 並傳回搜尋結果
# 第一個參數會是 newsapi 所需要的 apikey
# 第二個參數則是要搜尋的關鍵字

#'title': 新聞標題 , 
#'content': 新聞摘要 ,
#'url': 網址 , 
#'publishedtime': 發布時間 

from flask import jsonify
import requests
import json

apikey = 'ab9b50bfa2164561974d16942e1b86a7'
apibaseurl = 'https://newsapi.org/v2/'
#設定起始日期
# date_start = '2022-01-01'
#設定結束日期
# date_end = '2023-03-30'

#搜尋頭條新聞
def search_top(keyword):
    url = apibaseurl + 'top-headlines'
    params = {'q': keyword, 'apiKey': apikey, 'country': 'tw' }
    response = requests.get(url, params=params)
    return json.loads(response.text)

#搜尋所有新聞
def search(keyword):
    url = apibaseurl + 'everything'
    params = {'q': keyword, 'apiKey': apikey}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        json_response = json.loads(response.text)
        # print(json_response)
        news_lists = []
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
    result = search('郭台銘')
    print(result)
    # #回傳狀態
    # print(result['status'])
    # #總共有幾則新聞
    # print(result['totalResults'])
    # #articles文章陣列  
    # for article in result['articles']:
    #     #來源
    #     print(article['source']['name'])
    #     #作者
    #     print(article['author'])
    #     #標題
    #     print(article['title'])
    #     #內容
    #     print(article['content'])
    #     #網址
    #     print(article['url'])
    #     #圖片
    #     print(article['urlToImage'])
    #     #發布時間
    #     print(article['publishedAt'])
    #     #來源
    #     print(article['source']['name'])
    #     print('-----------------------')