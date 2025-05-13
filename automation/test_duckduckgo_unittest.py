import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DuckDuckGoTest(unittest.TestCase):

    def setUp(self):
        service = Service(executable_path="automation/chromedriver.exe")
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("https://duckduckgo.com/")

    def test_search_python(self):
        wait = WebDriverWait(self.driver, 15)

        # Espera a que el input esté listo
        search_box = wait.until(EC.element_to_be_clickable((By.ID, "searchbox_input")))
        search_box.send_keys("Python programming language")

        # Encuentra y hace clic en el botón de búsqueda
        search_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        search_button.click()

        # Esperar a que el título contenga "Python"
        wait.until(EC.title_contains("Python"))

        self.assertIn("Python", self.driver.title)
        print("✅ DuckDuckGo: ¡La búsqueda funcionó perfectamente!")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()