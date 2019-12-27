# wangyiMusicSpider
结合mitmpoxy(抓包工具)、selenium、python(requests库)爬取网易云音乐排行榜
## 1、分析网页(chrome浏览器)
 访问(https://music.163.com/#/discover/toplist) ,按键F12打开开发者工具，选择过滤XHR，然后点击任意一个音乐播放按钮
            ![](https://github.com/fuxiaofeng08/wangyiMusicSpider/blob/master/pic/20191227133853.jpg)
 红色圈文件正是音乐文件，在从其他请求文件中查找response中存在这个文件的request请求，发现绿色(https://music.163.com/weapi/song/enhance/player/url/v1?) response中包含，
