from selenium.webdriver.common.by import By

# first popup for new user 
USER_AGREE = (By.XPATH, '//span[text()="Zaakceptuj Wszystko"]')

# search field and button
SEARCH_INPUT = (By.ID, 'searchboxinput')
SEARCH_BUTTON =(By.XPATH, '//button[@id="searchbox-searchbutton"]')

# search results
RESULTS_CONTAINER = (By.XPATH, '//div[contains(@aria-label, "Wyniki dla zapytania")]')
RESULTS = (By.XPATH, '//div[contains(@aria-label, "Wyniki dla zapytania")]/div/div/a')

# results page ---> requires gMaps locator changes to be up to date
TITLE = (By.XPATH, '//h1[contains(@class, "header-title")]')
ADRESS = (By.XPATH, '//*[@data-item-id]')
WEBSITE = (By.XPATH, '//*[@data-item-id = "authority"]')
PHONE = (By.XPATH, '//*[@data-tooltip = "Kopiuj numer telefonu"]')