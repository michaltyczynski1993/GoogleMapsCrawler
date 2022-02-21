from selenium.webdriver.common.by import By

# first popup for new user 
USER_AGREE = (By.XPATH, '//span[text()="Zgadzam się"]')

# search field and button
SEARCH_INPUT = (By.ID, 'searchboxinput')
SEARCH_BUTTON =(By.XPATH, '//button[@id="searchbox-searchbutton"]')