from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import locators
from bs4 import BeautifulSoup


options = Options()
# options.add_argument("--headless")
driver = webdriver.Chrome(service=Service('C:\TestFiles\chromedriver.exe'), options=options)
driver.implicitly_wait(10)

driver.get('https://www.google.pl/maps/place/Ninja+Bar/@52.3067903,21.0303654,17z/data=!3m1!4b1!4m5!3m4!1s0x471ec9337b2fe86d:0x737b6129293a4844!8m2!3d52.3067903!4d21.0303654?authuser=0&hl=pl')
try:
    button = driver.find_element(*locators.USER_AGREE)
    button.click()
except:
    print('button is not clickable')

# wait for site to load
WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locators.TITLE))

soup = BeautifulSoup(driver.page_source, 'html.parser')
phone_adress_results = soup.find_all('div', class_ = 'Io6YTe')
#locating elements on single result page
title = soup.find('h1', class_ = 'DUwDvf')
rating = soup.find('div', class_ = 'F7nice')
category = soup.find('button', class_ = 'DkEaL')
adress = phone_adress_results[0]
phone = phone_adress_results[1]
website = soup.find('div', class_ = 'rogA2c')

for result in phone_adress_results:
    print(result.text.strip())
# print(title.text.strip())
# print(rating.text.strip())
# print(category.text.strip())
# print(website.text.strip())
# print(adress.text.strip())
# print(phone.text.strip())