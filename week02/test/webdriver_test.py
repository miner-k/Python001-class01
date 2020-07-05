
from selenium import webdriver
import time

try:

    browser = webdriver.Chrome()

    browser.get("https://shimo.im/login?from=home")

    time.sleep(3)
    user = 'xxxxxxx'
    password = 'xxxxxxx'
    browser.find_element_by_xpath('//div[@type="mobileOrEmail"]/div[@class="input"]/input').send_keys(user)
    browser.find_element_by_xpath('//div[@type="password"]/div[@class="input"]/input').send_keys(password)
    browser.find_element_by_xpath('//button[@type="black"]').click()

    time.sleep(9)
except Exception as  e:
    print(e)
finally:
    browser.close()

