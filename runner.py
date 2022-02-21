from msilib.schema import Class
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(executable_path='C:\TestFiles\chromedriver.exe')
driver.implicitly_wait(20)
driver.get('https://www.google.pl/maps/preview')

# jeśli pojawi się przycisk zgadzam się to go kliknij
button = driver.find_element(By.XPATH, '//span[text()="Zgadzam się"]')

if button.is_displayed():
    button.click()
else:
    print('button zgadzam sie is not displayed')

# znajdź input wprowadź swój tekst i wciśnij button wyszukaj

user_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'searchboxinput')))
user_input.send_keys("Sklep Warszawa")
time.sleep(3)
submit_button = driver.find_element(By.XPATH, '//button[@id="searchbox-searchbutton"]')
submit_button.click()
time.sleep(3)

# find div with search results
elements = driver.find_elements(By.XPATH, '//div[contains(@aria-label, "Wyniki dla zapytania")]/div/div/a')

# open first element from 'elements' list in new tab - using Actionchains CTRL+click()
actions = ActionChains(driver)
actions.move_to_element(elements[0])
actions.key_down(Keys.CONTROL).click()
actions.perform()