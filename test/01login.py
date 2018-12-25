import requests
import urllib.request
from urllib import request,parse
from lxml import etree
import http.cookiejar


class Login(object):
    def __init__(self):
        self.headers = {
            'Referer': 'https://creditshop.hxb.com.cn/mall/member/loginSSL.action/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
            'Host': 'github.com'
        }
        self.login_url = 'https://creditshop.hxb.com.cn/mall/member/loginSSL.action'
        # self.post_url = 'https://github.com/session'
        self.logined_url = 'https://creditshop.hxb.com.cn/mall/member/index.action'
        self.session = requests.Session()
        self.cookie = http.cookiejar.CookieJar()
        self.handler = request.HTTPCookieProcessor(self.cookie)
        self.opener = request.build_opener(self.handler)

    # def token(self):
    #     response = self.session.get(self.login_url, headers=self.headers)
    #     selector = etree.HTML(response.text)
    #     # token = selector.xpath('//div//input[2]/@value')
    #     token = selector.xpath("//div[(@class='details_register_2')]")
    #     return token

        # 验证码获取
    def ver_code(self):
        response = urllib.request.urlopen(self.login_url,headers = self.headers)
        # response = self.session.get(self.login_url, headers=self.headers)
        selector = etree.HTML(response.text)
        # imgurl = "https://creditshop.hxb.com.cn" + selector.xpath("//div[(@class='details_register_2')]//img[1]/@src")
        #验证码url
        imgurl = "https://creditshop.hxb.com.cn" + selector.xpath(".//div[(@class='details_register_2')]//img[(@id='imgCode')]/@src")
        print(imgurl)
        imgs = request.urlretrieve(imgurl, "./yanzheng.jpg")

        # i = range(100)
        # img = imgurl
        # try:
        #     pic = requests.get(img, timeout=5)  # 超时异常判断 5秒超时
        # except requests.exceptions.ConnectionError:
        #     print('当前图片无法下载')
        # file_name = "image/" + "验证码"+str(i) + ".jpg"  # 拼接图片名
        # print(file_name)
        # # 将图片存入本地
        # fp = open(file_name, 'wb')
        # fp.write(pic.content)  # 写入图片
        # fp.close()
        imgcode = input("请输入验证码:")
        return imgcode

    #登录
    def login(self, loginNumber, password,imgcode=None):
        data = {
            'returnURL':'',
            'loginNumber': loginNumber,
            'loginPwd': password,
            'imgCode':imgcode,
            'loginAnswer':'',
            'x':'85',
            'y':'26',
        }
        data = parse.urlencode(data).encode('utf-8')
        response = requests.Request(url =self.login_url,data = data,headers=self.headers)
        # res = self.opener.open(response)  # 保存cookie信息
        # print(res.read())
        # response = self.session.get(self.post_url, data=data, headers=self.headers)


        #登录后页面抓取
    def logined(self, opener=None):
        #页面请求
        # req = requests.Request(url=self.self.logined_url,headers=self.headers)
        req = urllib.request.urlopen(self.logined_url,headers=self.headers)
        print(req.read().decode('utf-8'))
        res = opener.open(req)
        with open("info.html", "wb") as fp:
            fp.write(res.read())
        # if response.status_code == 200:
        #     self.dynamics(response.text)
        #
        # response = self.session.get(self.logined_url, headers=self.headers)
        # if response.status_code == 200:
        #     self.profile(response.text)

    # def dynamics(self, html):
    #     selector = etree.HTML(html)
    #     dynamics = selector.xpath('//div[contains(@class, "news")]//div[contains(@class, "alert")]')
    #     for item in dynamics:
    #         dynamic = ' '.join(item.xpath('.//div[@class="title"]//text()')).strip()
    #         print(dynamic)

    # def profile(self, html):
    #     selector = etree.HTML(html)
    #     name = selector.xpath('//input[@id="user_profile_name"]/@value')[0]
    #     email = selector.xpath('//select[@id="user_profile_email"]/option[@value!=""]/text()')
    #     print(name, email)



if __name__ == "__main__":
    login = Login()
    # imgcode = input("请输入验证码:")
    login.login(loginNumber='6259691129820511', password='zc006699')
