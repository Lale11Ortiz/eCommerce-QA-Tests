import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WikipediaTest(unittest.TestCase):

    def setUp(self):
        service = Service(executable_path="automation/chromedriver.exe")
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("https://en.wikipedia.org/")

    def test_search_python(self):
        wait = WebDriverWait(self.driver, 10)

        # Espera hasta que el input sea visible e interactuable
        search_box = wait.until(EC.element_to_be_clickable((By.NAME, "search")))
        search_box.send_keys("Python (programming language)")
        search_box.submit()

        # Espera a que se cargue el nuevo encabezado
        heading = wait.until(EC.visibility_of_element_located((By.ID, "firstHeading"))).text

        self.assertIn("Python", heading)
        print("✅ Se encontró la página correctamente.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()