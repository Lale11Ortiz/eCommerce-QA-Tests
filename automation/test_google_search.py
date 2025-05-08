from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Abrir el navegador
driver = webdriver.Chrome()

# Ir a Google
driver.get("https://www.google.com")

# Esperar a que cargue (opcional)
time.sleep(2)

# Encontrar la barra de búsqueda
search_box = driver.find_element(By.NAME, "q")

# Escribir algo
search_box.send_keys("Hola mundo")

# Presionar Enter
search_box.send_keys(Keys.RETURN)

# Esperar para ver resultados
time.sleep(3)

# Cerrar el navegador
driver.quit()