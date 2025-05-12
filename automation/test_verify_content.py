import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

class TestVerifyContent(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service("automation/chromedriver.exe"))
        self.driver.maximize_window()

    def test_content_present(self):
        driver = self.driver
        driver.get("https://en.wikipedia.org/")

        body_text = driver.find_element(By.TAG_NAME, "body").text.lower()
        expected_text = "the free encyclopedia that anyone can edit"

        self.assertIn(expected_text, body_text)
        print("✅ El contenido se encontró correctamente.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()