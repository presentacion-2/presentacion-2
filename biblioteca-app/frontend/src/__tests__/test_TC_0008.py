from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import FirefoxOptions
import time

def test_TC_0008():
    opts = FirefoxOptions()
    opts.add_argument("--headless")
    driver = webdriver.Firefox(options=opts)
    driver.maximize_window()
    driver.get("http://localhost:3000/")

    # Test Case: TC_0008
    wait = WebDriverWait(driver, 10)

    if(driver.title != "React App"):
        print("Fail")
        driver.close()

    usuario = driver.find_element("id","inputUsernameLogin")
    password = driver.find_element("id","inputPasswordLogin")

    usuario.clear()
    password.clear()
    usuario.send_keys("test1@gmail.com")
    password.send_keys("123")

    boton = driver.find_element('xpath','//*[@id="root"]/div/div[2]/form/button')
    boton.click()


    #buscar = driver.find_element("id","books")
    buscar = wait.until(EC.presence_of_element_located(("id", "books")))
    buscar.clear()
    buscar.send_keys("El principito")

    select_element = driver.find_element("id", 'filter')
    select = Select(select_element)


    filtro = driver.find_element(By.CSS_SELECTOR, 'option[value=titulo]')

    select.select_by_visible_text('Titulo')
    assert filtro.is_selected()

    botonBuscar = driver.find_element("xpath",'//*[@id="root"]/div/div/div[1]/form/button')
    botonBuscar.click()


    # Localizar la tabla

    table = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div/div[2]/table')))

    # Verificar si la tabla está vacía
    rows = table.find_elements("xpath",'//*[@id="root"]/div/div/div[2]/table/tbody/tr')

    try:
        assert len(rows) == 0
        print("La tabla está vacía.")
    except AssertionError:
        print("La tabla no está vacía.")


    driver.close()

