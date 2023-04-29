import requests
import xml.etree.ElementTree as ET
from flask import Flask

app = Flask(__name__)

# Specify the RSS feed URL
# RSS_URL = 'https://news.ltn.com.tw/rss/all.xml'       #OK
RSS_URL = 'https://news.ltn.com.tw/rss/politics.xml'

@app.route("/")
def news():
    # Fetch the RSS feed
    response = requests.get(RSS_URL)
    if response.status_code == 200:
        # Parse the XML response
        root = ET.fromstring(response.content)

        # Extract news article information from the RSS feed
        news_list = []
        for item in root.findall('./channel/item'):
            title = item.find('title').text
            link = item.find('link').text

            # Check if the 'description' element exists
            description_element = item.find('description')
            if description_element is not None:
                description = description_element.text
            else:
                description = 'No description available'

            # Check if the 'pubDate' element exists
            pub_date_element = item.find('pubDate')
            if pub_date_element is not None:
                pub_date = pub_date_element.text
            else:
                pub_date = 'No publish date available'

            # Add the news article information to the list
            news_list.append({'title': title, 'link': link, 'description': description, 'pub_date': pub_date})

        # Render the news articles as HTML
        html = '<html><body>'
        for news_item in news_list:
            html += '<h2>' + news_item['title'] + '</h2>'
            html += '<p><b>Link:</b> <a href="' + news_item['link'] + '">' + news_item['link'] + '</a></p>'
            html += '<p><b>Description:</b> ' + news_item['description'] + '</p>'
            html += '<p><b>Publish Date:</b> ' + news_item['pub_date'] + '</p>'
            html += '<hr>'
        html += '</body></html>'

        return html
    else:
        return 'Failed to fetch news articles. Response code:', response.status_code

if __name__ == "__main__":
    app.run()
