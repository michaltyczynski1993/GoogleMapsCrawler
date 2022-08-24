from re import search
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time
import locators
import timeit
#setup
search_region = input('enter searching region: ')
search_data = input('enter keywords: ')
search_links = []

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
    print('button is not clickable')

# first data input for locating searching region
user_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(locators.SEARCH_INPUT))
user_input.send_keys(search_region)
submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(locators.SEARCH_BUTTON))
submit_button.click()
time.sleep(8)

# take string to search in google maps results
user_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(locators.SEARCH_INPUT))
user_input.clear()
user_input.send_keys(search_data)
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

# print the found links (to gmaps sites)
for link in search_links:
    print(link)
print(len(search_links))

stop = timeit.default_timer()
print('Time: ', stop - start)
