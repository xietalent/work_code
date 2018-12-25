
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from scrapy.http import HtmlResponse
from logging import getLogger
from aip import AipOcr
from time import sleep
import lxml
from lxml import etree
import pytesseract
import pytesseract.pytesseract
from urllib import request
from PIL import Image

class SeleniumMiddleware():
    def __init__(self,timeout=None,service_args=[]):
        self.logger = getLogger(__name__)
        self.timeout = timeout
        # self.browser = webdriver.PhantomJS()
        self.browser = webdriver.Chrome()

    def __del__(self):
        self.browser.close()

    # def process_request(self,request,spider):
    def process_request(self):
        self.logger.debug('PhantomJS is Starting')
        # page = request.meta.get("https://creditshop.hxb.com.cn/mall/member/loginSSL.action")

        self.browser.get("https://perbank.abchina.com/EbankSite/startup.do")
        # self.browser.get("https://creditshop.hxb.com.cn/mall/member/doLogin.action")
        sleep(3)
        page_html2 = self.browser.page_source
        # print("当前网址"+self.browser.page_source)
        # return page_html

        #验证码url获取并下载
        # response = etree.HTML(page_html2)
        # divs = response.xpath(".//div[@class='details_register']")
        # imens = []
        # # imem = {}
        # for div in divs :
        #     imurl =div.xpath(".//tr[3]/td[@class='details_register_5 details_register_8']/img/@src")
        #     print(imurl)
            # imem={
            #     "imurl":imurl
            # }
            # imens.append(imem)
            # print(imem)
            # imens.append(imurl)
        # imurl = imem["imurl"]
        # print(imurl)
        # imurl1 = imens[0]
        # imurl1 = str(imurl1)
        # imurl = imurl1[2:-2]
        # img_url = "https://creditshop.hxb.com.cn" +imurl
        # img_url = "https://creditshop.hxb.com.cn" +"/mall/base/validateImg.action?type=dynamicImgCode"
        # print(img_url)
        # imgs = request.urlretrieve(img_url, "./imcode.jfif")
        # sleep(2)


#截取验证码的截图
        location = self.browser.find_element_by_id("imgCode").location
        self.browser.save_screenshot("feng.png")
        page_snap_obj = Image.open("feng.png")

        size = self.browser.find_element_by_id("imgCode").size
        left = location['x']
        top = location['y']
        right = location['x'] + size['width']
        bottom = location['y'] + size['height']

        imgages = page_snap_obj.crop((left, top, right, bottom))
        imgages.save("imcode.png")
        # imgages.show()
        # self.browser.save_screenshot("jifen02.png")


        #t验证码处理
        # image = PIL.Image.open(r"E:\code\test\imcode.png")
        # # image=PIL.Image.open(r"C:\Users\Administrator\Desktop\5107.jfif")
        # # pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
        # # 灰度化
        # image = image.convert('L')
        # # 杂点清除掉。只保留黑的和白的。返回像素对象
        # data = image.load()
        # w, h = image.size
        # for i in range(w):
        #     for j in range(h):
        #         if data[i, j] > 125:
        #             data[i, j] = 255  # 纯白
        #         else:
        #             data[i, j] = 0  # 纯黑
        # image.save('clean_captcha.png')
        # image.show()

        # ""
        # 你的
        # APPID
        # AK
        # SK
        # """
        APP_ID = '15188939'
        API_KEY = 'deq3Itvdip3GI42a4uazZcdD'
        SECRET_KEY = 'hwmuoK78LiC1mrIQdHBa42DWOGAHRAEo '

        client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

        """
        读取图片
        """
        def get_file_content(filePath):
            with open(filePath, 'rb') as fp:
                return fp.read()

        #定义参数变量
        options = {
            "recognize_granularity" :"big",
            "detect_direction": "true",
        }

        image = Image.open(r"E:\code\test\imcode.png")
        # image=PIL.Image.open(r"C:\Users\Administrator\Desktop\5107.jfif")

        # 灰度化
        image = image.convert('L')
        # 杂点清除掉。只保留黑的和白的。返回像素对象
        data = image.load()
        w, h = image.size
        for i in range(w):
            for j in range(h):
                if data[i, j] > 125:
                    data[i, j] = 255  # 纯白
                else:
                    data[i, j] = 0  # 纯黑
        image.save('clean_captcha.png')

        # image2 = get_file_content(r'C:\Users\Administrator\Desktop\7708.jfif')
        image2 = get_file_content('clean_captcha.png')
        # print(image2)
        """
        调用数字识别
        """
        result= client.numbers(image2)
        # for key in result:
        #     print(key,result[key])

        # print(result["words_result"][0]["words"])
        """
        如果有可选参数
        """

        client.numbers(image2, options)

        # result = pytesseract.pytesseract.image_to_string(image)
        print("验证码识别为:{}".format(result["words_result"][0]["words"])) #查看识别结果

        img_number = result["words_result"][0]["words"]

        self.browser.save_screenshot("jifen001.png")

        sleep(1)
        # imgcode = input("请输入验证码:{}".format(result))
        sleep(2)
        self.browser.find_element_by_id("doLogin_loginNumber").send_keys("6259691129820511")
        self.browser.find_element_by_id("doLogin_loginPwd").send_keys("zc006688")
        # self.browser.find_element_by_name("imgCode").send_keys("{}".format(imgcode))
        self.browser.find_element_by_name("imgCode").send_keys("{}".format(img_number))
        sleep(5)



       # 登录
        self.browser.find_element_by_id("doLogin_0").click()
        sleep(3)

        # 我的积分
        self.browser.find_element_by_id("leftMenu1").click()
        sleep(2)

        # 1  打开可用积分查询栏
        # self.browser.find_element_by_xpath("//div[(@class='details_member_left_box')][1]//li[1]/a/@href").click()
        self.browser.find_element_by_xpath("//div[(@class='details_member_left_box')][1]//li[1]/a").click()
        sleep(3)

        # 点击查询
        self.browser.find_element_by_class_name("inputBoxSubmit").click()
        sleep(2)
        self.browser.save_screenshot("jifen02.png")
        page_html = self.browser.page_source

        # print("当前网址"+self.browser.page_source)
        # return page_html
        items = []
        response = etree.HTML(page_html)
        divs = response.xpath(".//div[@class='details_member']/div[@class='details_member_right']")
        for div in divs:
            item = {}
            my_integral = div.xpath(".//div[@class='boundCarBox']//div/b/text()")[0]

            item = {
                "my_integral":my_integral,
            }
            items.append(item)
            print(my_integral)
            print(type(my_integral))
            print(items)




if __name__ == '__main__':
    s = SeleniumMiddleware()
    s.process_request()


