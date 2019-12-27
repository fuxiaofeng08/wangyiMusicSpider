# wangyiMusicSpider
结合mitmpoxy(抓包工具)、selenium、python(requests库)爬取网易云音乐排行榜
### 1、分析网页(chrome浏览器)
 访问(https://music.163.com/#/discover/toplist) ,按键F12打开开发者工具，选择过滤XHR，然后点击任意一个音乐播放按钮
            ![](https://github.com/fuxiaofeng08/wangyiMusicSpider/blob/master/pic/20191227133853.jpg)  
            红色圈文件正是音乐文件，在从其他请求文件中查找response中存在这个文件的request请求，发现绿色(https://music.163.com/weapi/song/enhance/player/url/v1?) response中包含，这个url请求中包含两个参数
            ![](https://github.com/fuxiaofeng08/wangyiMusicSpider/blob/master/pic/20191227142802.png)  
            网上有大神已经破译了这两个参数的加密方法，本文在与新手操作使用selenium模拟点击请求，然后使用mitmproxy抓包工具，抓取音乐文件的url
### 2、使用selenium模拟操作点击播放按钮
  ```pthon
  from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
chrome_options = Options()
chrome_options.add_argument('--proxy-server=127.0.0.1:9999')
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get("https://music.163.com/#/discover/toplist")
time.sleep(4)
driver.switch_to_frame("g_iframe")
ply = driver.find_elements_by_class_name("ply")
for i in range(1,len(ply)):
    print(ply[i].get_attribute("data-res-id"))
    driver.execute_script("arguments[0].click();", ply[i])
    time.sleep(0.5)
  ```
### 3、编写抓包策略，将截获的url保存在csv文件中
```python
target_url = "https://music.163.com/weapi/song/enhance/player/url/v1?csrf_token="
from mitmproxy import flow
import csv
import json
def response(flow):
    if flow.request.url.startswith(target_url):
        resp_data = json.loads(flow.response.text)
        id = resp_data.get("data")[0].get("id")
        url = resp_data.get("data")[0].get("url")
        print("-------------------------")
        print(id,url)
        print("-------------------------")
        with open("D:\\python_project\\pycharmPro\\proxy_test\\a.csv","a",newline="") as f:
            writer = csv.writer(f)
            writer.writerow([id,url])
    else:
        print("++++++++++++++++++++++++++++++++++++++++")
```
### 4、实现爬虫，从csv文件中读取url，下载排行榜音乐
```python
from threading import Thread
import csv
import requests
from queue import Queue

threadQueue = Queue()
url = "http://m10.music.126.net/20191115160601/0fb3b92225e0538899f1a472e81315dc/ymusic/010b/510f/0e58/6ad4671e1ffe09c97f7992874b925ccc.mp3"
def downLoad(id,url):
    r = requests.get(url)
    fileName = "D:\\python_project\\pycharmPro\\proxy_test\\" + url.split('/')[-1]
    with open(fileName,"wb") as f:
        f.write(r.content)
downLoad("asss",url)
```

## 程序运行顺序
 首先运行抓包工具，在抓包策略文件夹下运行mitmdump -s addons.py -p 9999(9999为指定的监听端口，与selenium配置的proxy参数对应)
 

