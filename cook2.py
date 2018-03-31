from selenium import webdriver
import time,pprint
base_url='http://bbs.lnd.com.cn/portal.php'
driver=webdriver.Chrome()
driver.implicitly_wait(10)

driver.get(base_url)

pprint.pprint(driver.get_cookies())
b=[{'domain': 'bbs.lnd.com.cn',
  'expiry': 1521792446.734303,
  'httpOnly': False,
  'name': 'FJUr_2132_checkpm',
  'path': '/',
  'secure': False,
  'value': '1'},
{'domain': 'bbs.lnd.com.cn',
  'expiry': 1553328416.882091,
  'httpOnly': False,
  'name': 'FJUr_2132_connect_is_bind',
  'path': '/',
  'secure': False,
  'value': '0'},
{'domain': 'bbs.lnd.com.cn',
  'expiry': 1524384378.856699,
  'httpOnly': True,
  'name': 'FJUr_2132_saltkey',
  'path': '/',
  'secure': False,
  'value': 'vN7x4eXC'},
{'domain': 'bbs.lnd.com.cn',
  'expiry': 1524384378.856937,
  'httpOnly': False,
  'name': 'FJUr_2132_lastvisit',
  'path': '/',
  'secure': False,
  'value': '1521788819'},
{'domain': 'bbs.lnd.com.cn',
  'expiry': 1521792680.028638,
  'httpOnly': False,
  'name': 'FJUr_2132_sendmail',
  'path': '/',
  'secure': False,
  'value': '1'},
{'domain': 'bbs.lnd.com.cn',
  'expiry': 1521792442.855312,
  'httpOnly': False,
  'name': 'FJUr_2132_checkfollow',
  'path': '/',
  'secure': False,
  'value': '1'},
{'domain': 'bbs.lnd.com.cn',
  'expiry': 1553328412.855174,
  'httpOnly': False,
  'name': 'FJUr_2132_lastcheckfeed',
  'path': '/',
  'secure': False,
  'value': '2227532%7C1521792453'},
{'domain': 'bbs.lnd.com.cn',
  'expiry': 1521878816.881926,
  'httpOnly': False,
  'name': 'FJUr_2132_lastact',
  'path': '/',
  'secure': False,
  'value': '1521792457%09misc.php%09patch'},
{'domain': 'bbs.lnd.com.cn',
  'httpOnly': False,
  'name': 'FJUr_2132_seccode',
  'path': '/',
  'secure': False,
  'value': '15536.4b6e2a5923e6b7b729'},
{'domain': '.bbs.lnd.com.cn',
  'expiry': 1553328416,
  'httpOnly': False,
  'name': 'Hm_lvt_db9e934ac7114509b638ce01d87444b4',
  'path': '/',
  'secure': False,
  'value': '1521792382'},
{'domain': 'bbs.lnd.com.cn',
  'expiry': 1524384412.854754,
  'httpOnly': True,
  'name': 'FJUr_2132_auth',
  'path': '/',
  'secure': False,
  'value': 'c34dXOLg063LPCqVzgOYiQvsYO5VILgpqmvBUhtRATagOMbohkC4eYu4pIMIOZmewe%2FQ%2BCBcQYD7oq1bB9LlqcvVfFDm'},
{'domain': 'bbs.lnd.com.cn',
  'expiry': 1553328412.854626,
  'httpOnly': False,
  'name': 'FJUr_2132_ulastactivity',
  'path': '/',
  'secure': False,
  'value': '1521792453%7C0'},
{'domain': 'bbs.lnd.com.cn',
  'httpOnly': False,
  'name': 'FJUr_2132_lip',
  'path': '/',
  'secure': False,
  'value': '113.133.217.194%2C1521792453'},
{'domain': 'bbs.lnd.com.cn',
  'expiry': 1521793016,
  'httpOnly': False,
  'name': 'FJUr_2132_noticeTitle',
  'path': '/',
  'secure': False,
  'value': '1'},
{'domain': '.bbs.lnd.com.cn',
  'httpOnly': False,
  'name': 'Hm_lpvt_db9e934ac7114509b638ce01d87444b4',
  'path': '/',
  'secure': False,
  'value': '1521792417'}]






driver.delete_all_cookies()
for i in b:
    driver.add_cookie(i)

time.sleep(4)
#打印登录后的cookie
driver.refresh()

















