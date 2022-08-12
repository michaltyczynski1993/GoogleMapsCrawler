from selenium.webdriver.common.by import By

# first popup for new user 
USER_AGREE = (By.XPATH, '//button/span')

# search field and button
SEARCH_INPUT = (By.ID, 'searchboxinput')
SEARCH_BUTTON =(By.XPATH, '//button[@id="searchbox-searchbutton"]')

# search results
RESULTS_CONTAINER = (By.XPATH, '//div[contains(@aria-label, "Wyniki dla zapytania")]')
RESULTS = (By.XPATH, '//div[contains(@aria-label, "Wyniki dla zapytania")]/div/div/a')

# results page ---> requires gMaps locator changes to be up to date
TITLE = (By.XPATH, '//h1/span[@jstcache]')
ADRESS = (By.XPATH, '(//div[@class = "rogA2c"]/div[contains(@class, "Io6YTe")])[1]')
WEBSITE = (By.XPATH, '(//div[contains(@class, "Io6YTe")])[3]')
PHONE = (By.XPATH, '(//div[contains(@class, "Io6YTe")])[4]')