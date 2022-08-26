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

driver.get('https://www.google.pl/maps/place/Pizzeria+San+Giovanni+-+pizza+na+telefon+Targ%C3%B3wek/@52.2916903,21.0505503,17z/data=!3m1!4b1!4m5!3m4!1s0x471ecebe9bdb2c75:0xe6135a0b32f9fdd5!8m2!3d52.2916903!4d21.0505503?authuser=0&hl=pl')
try:
    button = driver.find_element(*locators.USER_AGREE)
    button.click()
except:
    print('button is not clickable')

# wait for site to load
WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locators.TITLE))

soup = BeautifulSoup(driver.page_source, 'html.parser')
# phone_adress_results = soup.find_all('div', class_ = 'Io6YTe')
#locating elements on single result page
title = soup.find('h1', class_ = 'DUwDvf')
rating = soup.find('div', class_ = 'F7nice')
category = soup.find('button', {'jsaction':'pane.rating.category'})
adress = soup.find('button', {'data-item-id':'address'})
phone = soup.find('button', {'data-tooltip':'Kopiuj numer telefonu'}) # ---> better way to find specific locator
website = soup.find('a', {'data-tooltip':'Otwórz witrynę'})

print(title.text.strip())
print(rating.text.strip())
print(category.text.strip())
print(adress.text.strip())
print(website.text.strip())
print(phone.text.strip())