from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get('https://9gag.com/trending')
title_mem = driver.find_element('xpath', '(//*[@class="badge-evt badge-track"])[1]')
attr_mem = title_mem.get_attribute('href')
print(attr_mem)

with open('mem.txt', 'w') as mem_file:
    mem_file.write(attr_mem)