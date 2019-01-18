from selenium import webdriver

import time


driver = webdriver.Firefox(executable_path=r"D:\installPakge\drivers\geckodriver.exe")

driver.get("www.baidu.com")

time.sleep(10)

driver.close()


driver.quit()