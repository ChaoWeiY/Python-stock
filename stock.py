from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup


driver = webdriver.Chrome("./chromedriver.exe")
driver.implicitly_wait(10)
driver.get("https://goodinfo.tw/tw/")
number = driver.find_element_by_css_selector("#txtStockCode")
number.send_keys("2330")
button = driver.find_element_by_css_selector("input[type=submit]")
button.click()
time.sleep(2)
soup = driver.page_source
soup_html = BeautifulSoup(soup, "lxml")
table = soup_html.find_all("table", class_="b1 p4_2 r10")[0]
name = table.select("tr")[0].select("a")[0].text
data_date = table.select("tr")[0].select("td")[4].text[5:]
price = table.select("tr")[3].select("td")[0].text
volume = table.select("tr")[5].select("td")[0].text
hight = table.select("tr")[3].select("td")[6].text
low = table.select("tr")[3].select("td")[7].text
yclose = table.select("tr")[3].select("td")[1].text
yclose_volume = table.select("tr")[7].select("td")[0].text

print("公司名稱: " + name + "時間: " + data_date + "成交價: "+ price + "成交張數: " + volume + "最高: " + hight + "最低: " + low + "昨日收: " + yclose + "昨日張數: " + yclose_volume)

driver.quit()