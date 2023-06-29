from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import FirefoxOptions
import time

def test_TC_0001():
    # Configuración del driver y apertura de la página
    opts = FirefoxOptions()
    opts.add_argument("--headless")
    driver = webdriver.Firefox(options=opts)
    driver.maximize_window()
    driver.get("http://localhost:3000/")

    # Verificar el título de la página
    titulo_esperado = "React App"
    assert driver.title == titulo_esperado, f"El título obtenido '{driver.title}' no coincide con el esperado '{titulo_esperado}'"

    # Iniciar sesión
    usuario = driver.find_element("id", "inputUsernameLogin")
    password = driver.find_element("id", "inputPasswordLogin")

    usuario.clear()
    usuario.send_keys("test1@gmail.com")
    password.clear()
    password.send_keys("123")

    boton = driver.find_element("xpath", "//*[@id='root']/div/div[2]/form/button")
    boton.click()
    
    time.sleep(1)
    # Verificar la presencia del elemento en el navbar
    try:
        driver.find_element("css selector", '#navbarNavDropdown > ul > li:nth-child(1) > a')
        print("El elemento está presente en la página")
    except NoSuchElementException:
        raise AssertionError("El elemento no se encuentra en la página")
    
    try:
        driver.find_element("css selector", '#navbarNavDropdown > ul > li:nth-child(2) > a')
        print("El elemento está presente en la página")
    except NoSuchElementException:
        raise AssertionError("El elemento no se encuentra en la página")
    
    try:
        driver.find_element("css selector", '#navbarNavDropdown > ul > li:nth-child(3) > a')
        print("El elemento está presente en la página")
    except NoSuchElementException:
        raise AssertionError("El elemento no se encuentra en la página")
    
    # Verificar ausencia de elementos en el navbar
    try:
        driver.find_element("css selector", '#navbarNavDropdown > ul > li:nth-child(4) > a')
        raise AssertionError("Elemento inesperado está presente en la página")
    except NoSuchElementException:
        pass
    
    try:
        driver.find_element("css selector", '#navbarNavDropdown > ul > li:nth-child(5) > a')
        raise AssertionError("Elemento inesperado está presente en la página")
    except NoSuchElementException:
        pass

    # Cerrar el navegador
    driver.quit()
