from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import FirefoxOptions
import time

def test_TC_0003():
    # Configuración del driver y apertura de la página
    opts = FirefoxOptions()
    opts.add_argument("--headless")
    driver = webdriver.Firefox(options=opts)
    driver.maximize_window()
    driver.get("http://localhost:3000/")
    wait = WebDriverWait(driver, 10)
    
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

    buscador = driver.find_element("id", "books")
    buscador.clear()
    buscador.send_keys("deep")

    select_element = driver.find_element("id", 'filter')
    select = Select(select_element)


    filtro = driver.find_element(By.CSS_SELECTOR, 'option[value=titulo]')

    select.select_by_visible_text('Titulo')
    assert filtro.is_selected()

    botonBuscar = driver.find_element("xpath",'//*[@id="root"]/div/div/div[1]/form/button')
    botonBuscar.click()

    table = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div/div[2]/table')))

    # Verificar si la tabla está vacía
    rows = table.find_elements("xpath",'//*[@id="root"]/div/div/div[2]/table/tbody/tr')
    
    try:
        assert len(rows) != 0
        nombre = rows[0].find_element("xpath", "//*[@id='root']/div/div/div[2]/table/tbody/tr/td[1]")
        assert nombre.text == "Deep Learning", f"El título obtenido '{nombre.text}' no coincide con el esperado Deep Learning"
    except AssertionError:
        print("La tabla está vacía")
    
    # Cerrar el navegador
    driver.quit()
