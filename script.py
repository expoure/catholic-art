from bs4 import BeautifulSoup 
import requests
import os

def create_dir():
    # Directory
    dir_ = 'religion'
    # Parent Directory path
    parent_dir = os.path.dirname(os.path.realpath(__file__))
    # Path
    path = os.path.join(parent_dir, dir_)
    if os.path.exists(dir_):
        return path
    os.mkdir(path)
    return path

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

pageResponse = requests.get('https://santhatela.com.br/religiao/?et_per_page=500', headers=headers)
pageSoup = BeautifulSoup(pageResponse.text, "html.parser")
pageDivsTags = pageSoup.find_all('div', {'class': 'content-product'})
for div in pageDivsTags:
    imgUrl = div.find_all('img')[1]['srcset'].split(",", 10)[-1].split('jpg')[0] + 'jpg'
    response = requests.get(imgUrl)
    name = div.find_all('img')[1]['srcset'].split(",", 10)[-1].split('/')[-1].split('-d.jpg')[0]
    with open(create_dir() + "/" + name + '.png', 'wb') as handler:
        handler.write(response.content)
