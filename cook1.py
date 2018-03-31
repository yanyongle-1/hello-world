#coding=utf-8
from selenium import webdriver
import time
import pprint
base_url = "http://bbs.lnd.com.cn/portal.php"
usr_name = " "
usr_pwd = " "

driver = webdriver.Chrome()
driver.implicitly_wait(10)

#清除所有cookie
driver.delete_all_cookies()
driver.get(base_url)
pprint.pprint(driver.get_cookies())

driver.refresh()
driver.find_element_by_id('comiis_reg').click()
driver.find_element_by_name("username").send_keys(usr_name)
driver.find_element_by_name("password").send_keys(usr_pwd)
time.sleep(10)
#在这个等待的时间里去手动输入验证码


driver.find_element_by_id('loginsubmit').click()
time.sleep(2)
#打印登录后的cookie
pprint.pprint(driver.get_cookies())
