from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
chrome_options = Options()
chrome_options.add_argument('--proxy-server=127.0.0.1:9999')
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get("https://music.163.com/#/discover/toplist")
time.sleep(4)
driver.switch_to_frame("g_iframe")
ply = driver.find_elements_by_class_name("ply")
for i in range(1,len(ply)):
    print(ply[i].get_attribute("data-res-id"))
    driver.execute_script("arguments[0].click();", ply[i])
    time.sleep(0.5)
