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