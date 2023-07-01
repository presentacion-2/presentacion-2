from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
import time

def test_TC_0009():
    # Configuración del driver y apertura de la página
    options = Options()
    options.binary_location = r'C:\\Program Files\\Mozilla Firefox\\firefox.exe'
    driver = webdriver.Firefox(options=options)
    driver.maximize_window()
    driver.get("http://localhost:3000/")

    # Test Case: TC_0009
    wait = WebDriverWait(driver, 10)

    if(driver.title != "React App"):
        print("Fail")
        driver.close()

    usuario = driver.find_element("id","inputUsernameLogin")
    password = driver.find_element("id","inputPasswordLogin")

    usuario.clear()
    password.clear()
    usuario.send_keys("admin@gmail.com")
    password.send_keys("123")

    boton = driver.find_element('xpath','//*[@id="root"]/div/div[2]/form/button')
    boton.click()
    #Verificar que no existe el libro

    buscar = wait.until(EC.presence_of_element_located(("id", "books")))
    buscar.clear()
    buscar.send_keys("Hunger")

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
    except AssertionError:
        print("El libro ya existe.")
        driver.close()


    #Agregar libro
    agregar = wait.until(EC.presence_of_element_located(('xpath','//*[@id="navbarNavDropdown"]/ul/li[4]/a')))
    agregar.click()

    titulo = driver.find_element("id","titulo")
    autor = driver.find_element("id","autor")
    editorial = driver.find_element("id","editorial")
    ano = driver.find_element("id","año")
    descripcion = driver.find_element("id","descripcion")

    titulo.clear()
    autor.clear()
    editorial.clear()
    ano.clear()
    descripcion.clear()
    titulo.send_keys("The Hunger Games")
    autor.send_keys("Suzanne Collins")
    editorial.send_keys()
    ano.send_keys("2008")
    descripcion.send_keys()

    ingresar = driver.find_element("xpath",'//*[@id="root"]/div/div/form/button')
    ingresar.click()

    #Verificar que libro existe
    buscar = wait.until(EC.presence_of_element_located(("id", "books")))
    buscar.clear()
    buscar.send_keys("Hunger")

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
        assert len(rows) == 1
        print("El libro se agregó correctamente.")
    except AssertionError:
        print("El libro no se agregó correctamente.")
        driver.close()

    #Eliminar libro
    detalleLibro = wait.until(EC.presence_of_element_located(('xpath','//*[@id="root"]/div/div/div[2]/table/tbody/tr/td[4]/button')))
    detalleLibro.click()

    eliminar = wait.until(EC.presence_of_element_located(('xpath','//*[@id="root"]/div/div/div[2]/form/button')))
    eliminar.click()

    driver.close()