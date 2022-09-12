from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time
import locators
import timeit
import csv

#setup
search_data = input('enter keywords: ')
search_links = []
#list to store data
items_list = []
headers = ['Title', 'Rating', 'Category', 'Adress','Link', 'Telefon', 'Website']

options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(service=Service('C:\TestFiles\chromedriver.exe'), options=options)
driver.implicitly_wait(20)

# go to google maps main page and check for localization popup
start = timeit.default_timer()
driver.get('https://www.google.pl/maps/preview')
try:
    button = driver.find_element(*locators.USER_AGREE)
    button.click()
except:
    print('Cookies already accepted')

# take string to search in google maps results
user_input = WebDriverWait(driver, 30).until(EC.element_to_be_clickable(locators.SEARCH_INPUT))
user_input.clear()
user_input.send_keys(search_data)
submit_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable(locators.SEARCH_BUTTON))
submit_button.click()

# scrolling down all found google maps results
results_container = WebDriverWait(driver, 30).until(EC.visibility_of_element_located(locators.RESULTS_CONTAINER))
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
for link in search_links:
    print(link)
    print('')
    
# open every link in link list (scrape data) and close current window
for link in search_links:
    item = []
    driver.get(link)
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located(locators.TITLE))
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    # wait for page to load (title, rating, category, adress, phone, website) - if not then pass it
    try:
        title = soup.find('h1', class_ = 'DUwDvf')
        # element that contains the 'span' with rating text
        rating_container = soup.find('div', class_ = 'F7nice')
        rating = rating_container.find('span')
        category = soup.find('button', {'jsaction':'pane.rating.category'})
        adress = soup.find('button', {'data-item-id':'address'})
        try:
            phone = soup.find('button', {'data-tooltip':'Kopiuj numer telefonu'}) # ---> better way to find specific locator
        except:
            pass
        website = soup.find('a', {'data-tooltip':'Otwórz witrynę'})
        
    except:
        pass

    try:
        item.append(title.text.strip())
        item.append(rating.text.strip())
        item.append(category.text.strip())
        item.append(adress.text.strip())
        item.append(link)
        item.append(phone.text.strip())
        item.append(website.get('href'))
    except:
        pass

    items_list.append(item)

print(items_list)

# export data to csv
file = open('table.csv', 'w', newline='', encoding='utf-8')
writer = csv.writer(file)
writer.writerow(headers)
writer.writerows(items_list)
file.close()

stop = timeit.default_timer()
print('Time: ', stop - start)
driver.quit()

