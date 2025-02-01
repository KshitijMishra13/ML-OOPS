#https://python.langchain.com/docs/introduction/
#https://python.langchain.com/docs/concepts/
#https://python.langchain.com/docs/tutorials/

import threading
import requests
from bs4 import BeautifulSoup

urls = [
     'https://python.langchain.com/docs/introduction/',
     'https://python.langchain.com/docs/concepts/',
     'https://python.langchain.com/docs/tutorials/'
]

def fetch_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    print(soup.text)

threads = []

for url in urls:
    t = threading.Thread(target=fetch_content, args=(url,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print('Done')