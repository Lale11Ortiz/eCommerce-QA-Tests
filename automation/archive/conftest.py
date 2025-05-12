import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    # Setup
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")  # Opcional, saca si querés ver el navegador
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    yield driver

    # Teardown
    driver.quit()