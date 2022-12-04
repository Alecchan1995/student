from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
service = ChromeService(executable_path=ChromeDriverManager().install())
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option('useAutomationExtension', False)
chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(service=service,options=chrome_options)
driver.get("https://shopee.tw/")
time.sleep(1)
inputproduct = driver.find_element(By.CSS_SELECTOR,".shopee-searchbar-input__input")
inputproduct.send_keys("computer")
inputproduct.send_keys(Keys.RETURN)
time.sleep(1)
hight = 0
while True:
    hight +=1000
    try:
        driver.execute_script("window.scrollTo({},{})".format(0,hight))
        time.sleep(0.5)
        if hight == 6000:
            break
    except:
        break
soup = BeautifulSoup(driver.page_source,"html.parser")
prolist = soup.select(".col-xs-2-4.shopee-search-item-result__item")
print(len(prolist))