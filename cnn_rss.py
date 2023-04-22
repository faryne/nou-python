import requests
import xml.etree.ElementTree as ET

# Specify the RSS feed URL
# RSS_URL = 'http://rss.cnn.com/rss/edition.rss'      #OK
RSS_URL = 'http://rss.cnn.com/rss/cnn_topstories.rss'   #OK

# Fetch the RSS feed
response = requests.get(RSS_URL)
if response.status_code == 200:
    # Parse the XML response
    root = ET.fromstring(response.content)
    print('root=',root)
    # Extract news article information from the RSS feed
    for item in root.findall('./channel/item'):
        title = item.find('title').text
        link = item.find('link').text
        # description = item.find('description').text
        # pub_date = item.find('pubDate').text

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

        # Print the news article information
        print('Title:', title)
        print('Link:', link)
        print('Description:', description)
        print('Publish Date:', pub_date)
        print('---' * 10)
else:
    print('Failed to fetch news articles. Response code:', response.status_code)
