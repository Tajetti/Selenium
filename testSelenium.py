from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import os

# Configuração inicial
options = Options()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)

# Criação da pasta de evidências
pasta_evidencia = "evidencia"
os.makedirs(pasta_evidencia, exist_ok=True)

def tirar_screenshot(nome):
    driver.save_screenshot(os.path.join(pasta_evidencia, f"{nome}.png"))

try:
    # 1. Acessar site
    driver.get("https://www.saucedemo.com/")
    tirar_screenshot("01_homepage")

    # 2. Login
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(1)
    tirar_screenshot("02_pos_login")

    # 3. Adicionar 3 itens ao carrinho
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    tirar_screenshot("03_itens_adicionados")

    # 4. Ir ao carrinho
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    time.sleep(1)
    tirar_screenshot("04_carrinho")

    # 5. Checkout
    driver.find_element(By.ID, "checkout").click()
    time.sleep(1)
    tirar_screenshot("05_checkout_info")

    # 6. Preencher informações
    driver.find_element(By.ID, "first-name").send_keys("John")
    driver.find_element(By.ID, "last-name").send_keys("Doe")
    driver.find_element(By.ID, "postal-code").send_keys("123456")
    tirar_screenshot("06_formulario_preenchido")

    driver.find_element(By.ID, "continue").click()
    time.sleep(1)
    tirar_screenshot("07_resumo_compra")

    # 7. Finalizar compra
    driver.find_element(By.ID, "finish").click()
    time.sleep(1)
    tirar_screenshot("08_finalizado")

    print("Automação concluída com sucesso. Evidências salvas na pasta 'evidencia/'.")

except Exception as e:
    print("Ocorreu um erro:", e)

finally:
    driver.quit()
