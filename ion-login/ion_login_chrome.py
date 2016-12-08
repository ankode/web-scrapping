# code written by ANKUSH ANSHUMAN
# github.com/ankode

from selenium.webdriver import Chrome
b = Chrome('C:\\chromedriver.exe')
b.get('http://172.16.16.16/logout')
b.find_element_by_name("username").send_keys("")
b.find_element_by_name("password").send_keys("")
b.find_element_by_name("login").click()