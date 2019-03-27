
import requests
from time import sleep


class Logins():
    def __init__(self):
        pass

    def logins(self):
        url = "https://passport.weibo.cn/signin/login?"
        username= '15071469916'
        password = 'zc006688'
        userAgent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
        headers = {
            'Cookie':'_T_WM=b446b8261cd6b1f8e5adb117b0a2be2b; login=1d143a736fdf93d35dc1b24d4482f559',
            # 'Host':'passport.weibo.cn',
            # 'Origin':'https://passport.weibo.cn',
            'Referer':'https://passport.weibo.cn/signin/login?entry=mweibo&r=https%3A%2F%2Fweibo.cn%2F&backTitle=%CE%A2%B2%A9&vt=',
            'User-Agent':userAgent,
            # 'X-Requested-With':"XMLHttpRequest",
        }
        data = {
            'username':username,
            'password':password,
            'savestate':'1',
            'r':'https://weibo.cn/',
            'ec':'0',
            'pagerefer':'https://weibo.cn/pub/?vt=',
            'entry':'mweibo',
            'mainpageflag':'1',
            'hff':'',
            'hfp':'',
        }
        response = requests.get(url=url,data=data,headers=headers)
        print(f"statusCode = {response.status_code}")
        print(f"text = {response.text}")
    def start(self):
        self.logins()


if __name__ == '__main__':
    run_login = Logins()
    run_login.start()