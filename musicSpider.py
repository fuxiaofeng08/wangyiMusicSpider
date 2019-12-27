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