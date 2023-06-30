from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options

def test_TC_0006():
    # Configuración del driver y apertura de la página
    options = Options()
    options.binary_location = r'C:\\Program Files\\Mozilla Firefox\\firefox.exe'
    driver = webdriver.Firefox(options=options)
    driver.maximize_window()
    driver.get("http://localhost:3000/")

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

    #Buscar libro que se quiere modificar

    buscar = wait.until(EC.presence_of_element_located(("id", "books")))
    buscar.clear()
    buscar.send_keys("Deep")

    select_element = driver.find_element("id", 'filter')
    select = Select(select_element)


    filtro = driver.find_element(By.CSS_SELECTOR, 'option[value=titulo]')

    select.select_by_visible_text('Titulo')
    assert filtro.is_selected()

    botonBuscar = wait.until(EC.presence_of_element_located(("xpath",'//*[@id="root"]/div/div/div[1]/form/button')))
    botonBuscar.click()

    # Ingresamos a los detalles del libro

    botonIngresar = wait.until(EC.presence_of_element_located(("xpath",'//*[@id="root"]/div/div/div[2]/table/tbody/tr/td[4]/button')))
    botonIngresar.click()

    botonEditar = wait.until(EC.presence_of_element_located(("xpath",'//*[@id="root"]/div/div/div[2]/button')))
    botonEditar.click()

    # Modificamos el estado del libro
    select_disp = driver.find_element("id", 'estado')
    selectd = Select(select_disp)


    dispo = driver.find_element(By.CSS_SELECTOR, 'option[value=Prestado]')

    selectd.select_by_visible_text('Prestado')
    assert dispo.is_selected()

    botonGuardar = wait.until(EC.presence_of_element_located(("xpath",'//*[@id="root"]/div/div/div/form/button')))
    botonGuardar.click()

    # Verificamos que el libro se haya modificado
    buscar = wait.until(EC.presence_of_element_located(("id", "books")))
    buscar.clear()
    buscar.send_keys("Deep")

    select_element = driver.find_element("id", 'filter')
    select = Select(select_element)


    filtro = driver.find_element(By.CSS_SELECTOR, 'option[value=titulo]')

    select.select_by_visible_text('Titulo')
    assert filtro.is_selected()

    botonBuscar = wait.until(EC.presence_of_element_located(("xpath",'//*[@id="root"]/div/div/div[1]/form/button')))
    botonBuscar.click()

    botonIngresar = wait.until(EC.presence_of_element_located(("xpath",'//*[@id="root"]/div/div/div[2]/table/tbody/tr/td[4]/button')))
    botonIngresar.click()

    estado = wait.until(EC.presence_of_element_located(("xpath",'//*[@id="root"]/div/div/div[1]/table/tbody/tr/td[3]/div')))
    assert estado.text == "Prestado" , 'No está prestado'
   
    # Buscar libro modificado y volverlo a su estado original

    botonEditar = wait.until(EC.presence_of_element_located(("xpath",'//*[@id="root"]/div/div/div[2]/button')))
    botonEditar.click()

    # Modificamos el estado del libro
    select_disp = driver.find_element("id", 'estado')
    selectd = Select(select_disp)


    dispo = driver.find_element(By.CSS_SELECTOR, 'option[value=Disponible]')

    selectd.select_by_visible_text('Disponible')
    assert dispo.is_selected()

    botonGuardar = wait.until(EC.presence_of_element_located(("xpath",'//*[@id="root"]/div/div/div/form/button')))
    botonGuardar.click()


    driver.close()
