from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Ruta al chromedriver
service = Service('./chromedriver.exe')
driver = webdriver.Chrome(service=service)

# Abrimos una página de prueba
driver.get('https://example.com')

# Esperamos 5 segundos para ver que se cargó
time.sleep(5)

# Cerramos el navegador
driver.quit()