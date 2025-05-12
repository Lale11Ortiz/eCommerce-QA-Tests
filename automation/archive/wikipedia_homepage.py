from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WikipediaHomePage:
    URL = "https://en.wikipedia.org/"

    SEARCH_INPUT = (By.ID, "searchInput")      
    SEARCH_BUTTON = (By.ID, "searchButton")    
    HEADING = (By.ID, "firstHeading")

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get(self.URL)

    def search(self, text):
        print("DEBUG: Esperando a que cargue el input...")
        print(self.driver.page_source)
        wait = WebDriverWait(self.driver, 15)
        search_input = wait.until(EC.element_to_be_clickable(self.SEARCH_INPUT))
        search_input.clear()
        search_input.send_keys(text)
        search_button = wait.until(EC.element_to_be_clickable(self.SEARCH_BUTTON))
        search_button.click()

    def get_heading(self):
        return self.driver.find_element(*self.HEADING).text

    def verify_content(self):
        return "Python" in self.get_heading()