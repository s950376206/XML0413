from selenium import webdriver
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin
import time

import requests
driver = webdriver.Chrome('./chromedriver')
url = 'https://www.dcard.tw/f'
driver.get(url)

inputElement = driver.find_element_by_tag_name('input')
inputElement.send_keys('Python')

driver.find_element_by_css_selector('button.sc-1ehu1w3-2').click()
time.sleep(2)

html = driver.page_source
soup = bs(html, 'html.parser')

meta_datas = []
for x in soup.find_all('span', {'class': 'sc-6oxm01-2 hiTIMq'}):
    meta_datas.append(x.text.strip())
print(meta_datas)

forums = []
for i in range (len(meta_datas)):
    if 1 % 3 == 0:
        forums.append(meta_datas[i])

titles = []
for x in soup.find_all('h2',{'class': 'sc-1v1d5rx-3 eihOFJ'} ):
    titles.append((x.text))
print(titles)

hrefs = []
for x in soup.find_all('a',{'class': 'sc-1v1d5rx-4 gCVegi'}):
    hrefs.append(x['href'])

links = []
for href in hrefs:
    links.append(urljoin(url, href))
print(links)

for i in range(len(forums)):
    print(forums[i], titles[i], links[i])