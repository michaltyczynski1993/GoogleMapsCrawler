from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import locators

class Crawler(object):
    
    
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='C:\TestFiles\chromedriver.exe')
        self.driver.implicitly_wait(30)


class GoogleMapsCrawler(Crawler):

    def main_site(self):
        """go to google maps main page and check for localization popup"""
        self.driver.get('https://www.google.pl/maps/preview')
        button = self.driver.find_element(*locators.USER_AGREE)
        if button.is_displayed():
            button.click()
        else:
            print('button zgadzam sie is not displayed')
    
    
    def search(self, search_data = 'Sklep Warszawa'):
        """take string to search in google maps results"""
        user_input = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locators.SEARCH_INPUT))
        user_input.send_keys(search_data)
        time.sleep(3)
        submit_button = self.driver.find_element(*locators.SEARCH_BUTTON) 
        submit_button.click()
    
    
    def scroll_down_results(self):
        """scrolling down all found google maps results"""
        results_container = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locators.RESULTS_CONTAINER))
        verical_ordinate = 100
        for i in range(0, 31):
            print(verical_ordinate)
            self.driver.execute_script("arguments[0].scrollTop = arguments[1]", results_container, verical_ordinate)
            verical_ordinate += 100
            time.sleep(1)
    
    def open_results(self):
        """iterate on list of google maps results and open in new tab"""
        results = self.driver.find_elements(*locators.RESULTS)
        
        # open all elements from results list in new tab - using Actionchains CTRL+click()
        for i in range(len(results)-1):
            actions = ActionChains(self.driver)
            actions.move_to_element(results[i])
            actions.key_down(Keys.CONTROL).click()
            actions.perform()

g = GoogleMapsCrawler()
g.main_site()
g.search('restauracja witów')
g.scroll_down_results()
g.open_results()