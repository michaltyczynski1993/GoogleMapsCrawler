from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import csv
import time
import locators
import timeit

class Crawler(object):
    
    
    def __init__(self):
        self.options = Options()
        self.options.add_argument("--headless")
        self.driver = webdriver.Chrome(service=Service('C:\TestFiles\chromedriver.exe'), options=self.options)
        self.driver.implicitly_wait(30)


class GoogleMapsCrawler(Crawler):

    def __init__(self):
        super(GoogleMapsCrawler, self).__init__()
        self.csv_data = []
        self.start = None
        self.stop = None

    def main_site(self):
        """go to google maps main page and check for localization popup"""
        self.start = timeit.default_timer()
        self.driver.get('https://www.google.pl/maps/preview')
        try:
            button = self.driver.find_element(*locators.USER_AGREE)
            button.click()
        except:
            print('button is not clickable')
    
    
    def search(self, search_data = 'Sklep Warszawa'):
        """take string to search in google maps results"""
        user_input = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locators.SEARCH_INPUT))
        user_input.send_keys(search_data)
        # time.sleep(3)
        # submit_button = self.driver.find_element(*locators.SEARCH_BUTTON) 
        submit_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locators.SEARCH_BUTTON))
        submit_button.click()
    
    
    def scroll_down_results(self):
        """scrolling down all found google maps results"""
        results_container = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locators.RESULTS_CONTAINER))
        verical_ordinate = 100
        for i in range(0, 17):
            self.driver.execute_script("arguments[0].scrollTop = arguments[1]", results_container, verical_ordinate)
            verical_ordinate += 200
            time.sleep(1)
    
    def open_results(self):
        """iterate on list of google maps results and open in new tab"""
        results = self.driver.find_elements(*locators.RESULTS)
        
        # open all elements from results list in new tab - using Actionchains CTRL+click()
        for i in range(len(results)):
            actions = ActionChains(self.driver)
            actions.move_to_element(results[i])
            actions.key_down(Keys.CONTROL).click()
            actions.perform()
    
    def get_geolocators(self):
        """find geolocators and save in 'list', then export to 'csv_data' list"""
        list = []
        try:
            title = self.driver.find_element(*locators.TITLE)
            adress = self.driver.find_element(*locators.ADRESS)
            website = self.driver.find_element(*locators.WEBSITE)
            phone = self.driver.find_element(*locators.PHONE)
        except:
            pass
        
        try:
            list.append(title.text)
            list.append(adress.text)
            list.append(website.text)
            list.append(phone.text)
        except:
            pass
        self.csv_data.append(list)

    def export_csv(self, file_path):
        """export data from list to csv file"""
        header = ['Nazwa', 'Adres', 'Email', 'Telefon']
        file = open(file_path, 'w', newline='', encoding='utf-8')
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(self.csv_data)
        file.close()
        self.stop = timeit.default_timer()
        print('Time: ', self.stop - self.start)

    def results_data_getter(self):
        """iterate all opend browser's tabs"""
        handles = self.driver.window_handles
        for i in range(len(handles)):
            if i > 0:
                self.driver.switch_to.window(handles[i])
                self.get_geolocators()

