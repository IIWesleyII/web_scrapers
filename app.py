from bs4 import BeautifulSoup
import requests

headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'}
url = 'http://watch.nbastream.tv/philadelphia-76ers-live-stream/'
response = requests.get(url, headers = headers)
soup = BeautifulSoup(response.text, 'lxml')

# print all the hidden re-direct srcs
for script in soup.find_all('iframe'):
    print(script.get('src'))

