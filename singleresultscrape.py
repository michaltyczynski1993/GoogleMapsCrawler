from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import locators
from bs4 import BeautifulSoup
import timeit


options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(service=Service('/home/mtycz/Dokumenty/chromedriver'), options=options)
driver.implicitly_wait(10)

start = timeit.default_timer()
driver.get('https://www.google.pl/maps/place/Byczek+-+sklep+w%C4%99dliny,+ryby,+sery,+warzywa,+produkty+bio,+eko,+zdrowa+%C5%BCywno%C5%9B%C4%87/data=!4m7!3m6!1s0x471eceb1c1c26c5b:0x3c5db4a8cbbcdcd4!8m2!3d52.2904047!4d21.0312232!16s%2Fg%2F11hbnv7870!19sChIJW2zCwbHOHkcR1Ny8y6i0XTw?authuser=0&hl=pl&rclk=1')
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
try:
    title = soup.find('h1', class_ = 'DUwDvf')
    rating = soup.find('div', class_ = 'F7nice')
    category = soup.find('button', {'jsaction':'pane.rating.category'})
    adress = soup.find('button', {'data-item-id':'address'})
    phone = soup.find('button', {'data-tooltip':'Kopiuj numer telefonu'}) # ---> better way to find specific locator
    website = soup.find('a', {'data-tooltip':'Otwórz witrynę'})
except:
    pass

try:
    print(title.text.strip())
    print(rating.text.strip())
    print(category.text.strip())
    print(adress.text.strip())
    print(website.text.strip())
    print(phone.text.strip())
except:
    pass
stop = timeit.default_timer()
print('Time: ', stop - start)

