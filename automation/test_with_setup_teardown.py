import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import os

class TestGoogleTitle(unittest.TestCase):

    def setUp(self):
        chrome_path = os.path.join(os.getcwd(), "automation", "chromedriver.exe")
        service = Service(executable_path=chrome_path)
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()

    def test_title(self):
        self.driver.get("https://www.google.com")
        self.assertIn("Google", self.driver.title)
        print("✅ Título verificado correctamente.")

    def tearDown(self):
        time.sleep(2)
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()