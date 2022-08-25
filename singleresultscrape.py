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

driver.get('https://www.google.pl/maps/place/Restauracja+Dziki+Zak%C4%85tek/@52.359584,20.9729986,17z/data=!3m1!4b1!4m5!3m4!1s0x471ec824a03e3779:0x12291771fa3d8b4b!8m2!3d52.359584!4d20.9751873')

try:
    button = driver.find_element(*locators.USER_AGREE)
    button.click()
except:
    print('button is not clickable')

# wait for site to load
WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locators.TITLE))

soup = BeautifulSoup(driver.page_source, 'html.parser')

#locating elements on single result page
title = soup.find('h1', class_ = 'DUwDvf')
rating = soup.find('div', class_ = 'F7nice')
adress = soup.find('div', class_ = 'Io6YTe')

print(title.text.strip())
print(rating.text.strip())
print(adress.text.strip())
