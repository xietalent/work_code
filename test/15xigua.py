from selenium import webdriver
from urllib.request import urlretrieve
import requests
from lxml import etree
from time import sleep
import random
import string

options  = webdriver.ChromeOptions()
options.add_argument('headless')

driver = webdriver.Chrome(chrome_options=options)

driver.implicitly_wait(10)

headers = {
    'referer': 'https://www.ixigua.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36'
}

url = 'https://www.ixigua.com/'


# 抓取第一个页面
driver.get(url)

a_list = driver.find_elements_by_xpath('//a[@class="img-wrap"]')
href_list = []
for a in a_list:
    href = a.get_attribute('href')
    href_list.append(href)



def random_str(size=64):
    base_str = string.ascii_letters + string.digits
    return ''.join(random.choice(base_str) for _ in base_str)


for href in href_list:
    response = requests.get(href, headers=headers)
    print(response.text)
    print(response.text.find('vjs_video_3_html5_api'))
    exit()
    html = etree.HTML(response.text)
    video_href = html.xpath('//video[@id="vjs_video_3_html5_api"]/@src')

    print(video_href)
    exit()
    urlretrieve(video_href, filename='./xigua/' + random_str() + '.mp4')



# for a in a_list:
#     a.click()
#     # 获取视频的地址
#     src = driver.find_element_by_tag_name('video').get_attribute('src')
#     # 下载
#     urlretrieve(src, filename='./xigua/' + random_str() + '.mp4')
#     driver.close()


