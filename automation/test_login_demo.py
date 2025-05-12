import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

class TestLoginDemo(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service("automation/chromedriver.exe"))
        self.driver.maximize_window()

    def test_login(self):
        driver = self.driver
        driver.get("https://practicetestautomation.com/practice-test-login/")

        driver.find_element(By.ID, "username").send_keys("student")
        driver.find_element(By.ID, "password").send_keys("Password123")
        driver.find_element(By.ID, "submit").click()

        # Verificamos que el login fue exitoso al ver si aparece el mensaje/post-login
        success_text = driver.find_element(By.TAG_NAME, "h1").text
        self.assertEqual(success_text, "Logged In Successfully")

        print("✅ Login exitoso y verificado.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()