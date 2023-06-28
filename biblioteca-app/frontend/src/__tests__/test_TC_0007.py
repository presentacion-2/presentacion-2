from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_TC_0007():
    # Configuración del driver y apertura de la página
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://localhost:3000/")
    wait = WebDriverWait(driver, 10)
    
    # Verificar el título de la página
    titulo_esperado = "React App"
    assert driver.title == titulo_esperado, f"El título obtenido '{driver.title}' no coincide con el esperado '{titulo_esperado}'"


    usuario = driver.find_element("id","inputUsernameLogin")
    password = driver.find_element("id","inputPasswordLogin")

    usuario.clear()
    password.clear()
    usuario.send_keys("admin@gmail.com")
    password.send_keys("123")

    boton = driver.find_element('xpath','//*[@id="root"]/div/div[2]/form/button')
    boton.click()
    
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
    editorial.send_keys("Scholastic Press")
    ano.send_keys("2008")
    descripcion.send_keys("The Hunger Games is a 2008 dystopian novel by the American writer Suzanne Collins. It is written in the voice of 16-year-old Katniss Everdeen, who lives in the future, post-apocalyptic nation of Panem in North America.")

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
    time.sleep(2)

    inicio = driver.find_element("css selector", '#navbarNavDropdown > ul > li:nth-child(1) > a')
    inicio.click()
    time.sleep(1)

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

    assert len(rows) == 0, f"Libro no eliminado"
    print("Libro eliminado correctamente")
    driver.close()

