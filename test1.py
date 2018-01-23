from selenium import webdriver

DRIVER = webdriver.Firefox()

DRIVER.get('https://www.baidu.com/')

DRIVER.quit()