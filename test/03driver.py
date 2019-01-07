from selenium import webdriver
from time import sleep
import lxml
driver = webdriver.Chrome()
# driver = webdriver.PhantomJS()

#打开百度
# driver.get("http://creditcard.hxb.com.cn/card/cn/index.shtml")
# driver.get("https://creditshop.hxb.com.cn/mall/member/loginSSL.action")
driver.get("https://creditcard.ecitic.com/citiccard/ucweb/entry.do")


#查找页面上的,并且点击
# driver.find_element_by_link_text("")[0].click()

sleep(4)
driver.save_screenshot("jifen001.png")
sleep(2)
imgcode = input("请输入验证码:")
sleep(2)
driver.find_element_by_id("doLogin_loginNumber").send_keys("6259691129820511")
driver.find_element_by_id("doLogin_loginPwd").send_keys("zc006688")
driver.find_element_by_name("imgCode").send_keys("{}".format(imgcode))
sleep(1)
# driver.find_element_by_link_text("登录")[0].click()
# driver.find_element_by_xpath("//div[@class='fliter-wp']/div/form/div/div/label[5]").click()
# driver.find_element_by_xpath("//div[(@class='details_register_2')]//input/@src").click()

#登录
driver.find_element_by_id("doLogin_0").click()

sleep(3)

#我的积分
driver.find_element_by_id("leftMenu1").click()
sleep(2)

#打开可用积分查询栏
# driver.find_element_by_xpath("//div[(@class='details_member_left_box')][1]//li[1]/a/@href").click()
driver.find_element_by_xpath("//div[(@class='details_member_left_box')][1]//li[1]/a").click()
# driver.find_element_by_id("details_member_left_box1").click()
sleep(3)



#点击查询
driver.find_element_by_class_name("inputBoxSubmit").click()

driver.save_screenshot("jifen02.png")
