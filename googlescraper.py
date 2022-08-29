from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time
import locators
import timeit
import pandas as pd
#setup
search_data = input('enter keywords: ')
search_links = []
#list to store data
templist = []

options = Options()
# options.add_argument("--headless")
driver = webdriver.Chrome(service=Service('C:\TestFiles\chromedriver.exe'), options=options)
driver.implicitly_wait(10)

# go to google maps main page and check for localization popup
start = timeit.default_timer()
driver.get('https://www.google.pl/maps/preview')
try:
    button = driver.find_element(*locators.USER_AGREE)
    button.click()
except:
    print('Cookies already accepted')

# take string to search in google maps results
user_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(locators.SEARCH_INPUT))
user_input.clear()
user_input.send_keys(search_data)
submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(locators.SEARCH_BUTTON))
submit_button.click()

# scrolling down all found google maps results
results_container = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locators.RESULTS_CONTAINER))
while True:
    # Get scroll height
    last_height = driver.execute_script("return arguments[0].scrollHeight", results_container)
    driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", results_container)
    time.sleep(3)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return arguments[0].scrollHeight", results_container)
    if new_height == last_height:
        break
    last_height = new_height

# find all results 
results = driver.find_elements(*locators.RESULTS)

# find links for every result
for result in results:
    link = result.get_attribute('href')
    search_links.append(link)

print(len(search_links))
# open every link in link list (scrape data) and close current window
for link in search_links:
    driver.get(link)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locators.TITLE))
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    # wait for page to load (title, rating, category, adress, phone, website) - if not then pass it
    try:
        title = soup.find('h1', class_ = 'DUwDvf')
        rating = soup.find('div', class_ = 'F7nice')
        category = soup.find('button', {'jsaction':'pane.rating.category'})
        adress = soup.find('button', {'data-item-id':'address'})
        phone = soup.find('button', {'data-tooltip':'Kopiuj numer telefonu'}) # ---> better way to find specific locator
        website = soup.find('a', {'data-tooltip':'Otwórz witrynę'})
        
    except:
        title = 'NULL'
        rating = 'NULL'
        category = 'NULL'
        adress = 'NULL'
        phone = 'NULL'
        website = 'NULL'


    try:
        Table_dict={ 'title': title.text.strip(),
                    'rating': rating.text.strip(),
                    'category': category.text.strip(),
                    'adress': adress.text.strip(),
                    'phone': phone.text.strip(),
                    'website': website.text.strip()}
            
        templist.append(Table_dict)
    except:
        pass

# export data to csv
df = pd.DataFrame(templist)
df.to_csv('table.csv')

stop = timeit.default_timer()
print('Time: ', stop - start)
driver.quit()

