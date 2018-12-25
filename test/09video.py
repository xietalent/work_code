import requests
from lxml import etree
from selenium import webdriver
from time import sleep
import json


# 定义一个函数用于处理页面
def handle_page(json_url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
    # 请求json_url
    r = requests.get(url=json_url,headers=headers)
    # print(r.text)
    obj = json.loads(r.text)
    video_list = obj["data"]
    # print(video_list)
    # 遍历video_list
    for video in video_list:
        # 获取视频的id
        video_id = video["video_id"]
        # 获取资源路径
        video_src = "https://365yg.com" + video["source_url"]
        # 获取视频连接，并处理
        handle_video(video_id,video_src)

# 封装一个函数用于处理视频
def handle_video(video_id,video_src):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}

    driver = webdriver.PhantomJS(r"C:\Users\fanjianbo\Desktop\phantomjs-2.1.1-windows\bin\phantomjs.exe")
    driver.get(video_src)
    sleep(5)
    page_source = driver.page_source
    # print(page_source)
    html_tree = etree.HTML(page_source)

    video_url = "http:" + html_tree.xpath('//video/source/@src')[0]
    # print(video_url)
    # 下载视频
    r = requests.get(video_url,headers=headers)
    filename = "./video/" + video_id + ".mp4"
    with open(filename,'wb') as fp:
        fp.write(r.content)
    print(filename+"下载完毕！")

def main():
    json_url = "https://365yg.com/api/pc/feed/?category=video&utm_source=toutiao&widen=3&max_behot_time=0&max_behot_time_tmp=0&tadrequire=true&as=A1253AF48A0FCE5&cp=5A4A4F4CAEE59E1&_signature="
    handle_page(json_url=json_url)
    pass

if __name__ == '__main__':
    main()


# 反爬机制：js动态加载、 隐藏资源数据连接、用户代理






