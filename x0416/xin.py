import requests

url = 'http://opendata.hccg.gov.tw/dataset/1f334249-9b55-4c42-aec1-5a8a8b5e07ca/resource/3f2d8472-7bae-48d0-909f-546591a34d34/download/20191231090605186.json'
html_content = requests.get(url)
json_content = html_content.json()

for a in json_content()
    ID = json_content.get("站點名稱")
    A = json_content.get('經度')
    B = json_content.get('緯度')
    URL = json_content.get("圖片URL")
    site = json_content.get('站點位置')

print(ID)
print(A)
print(B)
print(URL)
print(site)