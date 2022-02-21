from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import locators

class Crawler(object):
    
    
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='C:\TestFiles\chromedriver.exe')
        self.driver.implicitly_wait(30)


class GoogleMapsCrawler(Crawler):

    def main_site(self):
        self.driver.get('https://www.google.pl/maps/preview')
        button = self.driver.find_element(*locators.USER_AGREE)
        if button.is_displayed():
            button.click()
        else:
            print('button zgadzam sie is not displayed')
    
    def search(self, search_data = 'Sklep Warszawa'):
        user_input = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locators.SEARCH_INPUT))
        user_input.send_keys(search_data)
        time.sleep(3)
        submit_button = self.driver.find_element(*locators.SEARCH_BUTTON) 
        submit_button.click()

g = GoogleMapsCrawler()
g.main_site()
g.search('kawiarnie Warszawa')