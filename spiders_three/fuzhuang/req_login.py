
import requests
from time import sleep


class Logins():
    def __init__(self):
        pass

    def logins(self):
        session = requests.Session()
        url = "http://www.anta.cn/pass/login.html"
        username= '15071469916'
        password = '57c459f2a4fb8b5a3104a408c88dddb5'
        userAgent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
        headers = {
            'Cookie':'Hm_lvt_da161d8f61f938ec4aaa98a3a7075e6d=1551864687,1551867603,1552534981,1553561787; webshopsid=clptm1b4j2vkc30kmmjds9ro55; ANTA=ANtsQmr60wpdlzxVVsq7aA$$; 8ofOGk_think_language=zh-CN; Hm_lpvt_da161d8f61f938ec4aaa98a3a7075e6d=1553670320; __ozlvd1741=1553670322',
            'Referer':'http://www.anta.cn/pass/login.html',
            'User-Agent':userAgent,
            'X-Requested-With':"XMLHttpRequest",
        }
        data = {
            'username':username,
            'password':password,
        }
        response = session.get(url=url,data=data,headers=headers)
        print(f"statusCode = {response.status_code}")
        print(f"text = {response.text}")
    def start(self):
        self.logins()


if __name__ == '__main__':
    run_login = Logins()
    run_login.start()