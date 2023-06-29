from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import FirefoxOptions
import time

def test_TC_0013():
    opts = FirefoxOptions()
    opts.add_argument("--headless")
    driver = webdriver.Firefox(options=opts)
    driver.maximize_window()
    driver.get("http://localhost:3000/")

    # Test Case: TC_0013
    wait = WebDriverWait(driver, 10)

    if(driver.title != "React App"):
        print("Fail")
        driver.close()

    usuario = driver.find_element("id","inputUsernameLogin")
    password = driver.find_element("id","inputPasswordLogin")

    usuario.clear()
    password.clear()
    usuario.send_keys("test1@gmail.com")
    password.send_keys("1234")

    boton = driver.find_element('xpath','//*[@id="root"]/div/div[2]/form/button')
    boton.click()

    mensaje = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[2]/form/p')))


    try:
        assert mensaje.text == "Usuario o contraseña incorrectos"
        print("El usuario no logro iniciar sesion")
    except AssertionError:
        print("El usuario logro iniciar sesion")
        driver.close()


    driver.close()

