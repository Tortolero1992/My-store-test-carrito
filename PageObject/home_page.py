
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

url= "https://qalab.bensg.com/store/pe/"

class home_page:
         
    def __init__(self) :
        #localizadores
        self.driver = webdriver.Chrome()
        self.inisio_secion_link = '//span[@class="hidden-sm-down"]'
        self.correo = "field-email"
        self.contraseña = "field-password"
        self.inisio_secion_enter = "submit-login"
        self.categoria = '//a[@class="dropdown-item" and @href="https://qalab.bensg.com/store/pe/3-clothes"]'
        self.subcategoria = '//a[text()="Men"]'
        self.primer_elemento = '//a[@class="thumbnail product-thumbnail" and @href="https://qalab.bensg.com/store/pe/men/1-1-hummingbird-printed-t-shirt.html#/1-tamano-s/8-color-blanco"]'
        self.agregar_cantidad = '//input[@id="quantity_wanted"]'
        self.agregar_carrito = "//button[@class='btn btn-primary add-to-cart']"
   
    ##Funciones de la pagina## 

    #con esto iniciamos el buscador
    def webDriverGet(self):
        self.driver.maximize_window()
        self.driver.get(url)
    
    #con esto seleccionamos el campo para escrinir el correo
    def cuadro_correo(self, correo):
        correo_electronico = self.driver.find_element(By.ID, self.correo)
        correo_electronico.send_keys(correo)
    
    #conesto agregamos la contraseña para iniciar secion
    def cuadro_pass(self, contraseña):
        password = self.driver.find_element(By.ID, self.contraseña)
        password.send_keys(contraseña)
        
    #con esto borramos la cantidad de articulo y agregamos la cantodad deceada
    def agregar_mas_cantidad(self):
        agregar_cantidad = self.driver.find_element(By.XPATH, self.agregar_cantidad)
        agregar_cantidad.send_keys(Keys.CONTROL + 'a')
        agregar_cantidad.send_keys(Keys.BACKSPACE)
        agregar_cantidad.send_keys(2)
        
    #con esto damos click a iniciar secion en login page      
    def iniciar_secion(self):
        return self.driver.find_element(By.XPATH, self.inisio_secion_link).click()
    
    #conesto le damos enter al inicio de secion del login page
    def iniciar_secion_enter(self):
        return self.driver.find_element(By.ID, self.inisio_secion_enter).click()
    
    #con esto escogemos la categorias Clothes
    def categoria_clothes(self):
        return self.driver.find_element(By.XPATH, self.categoria).click()
    
    #con esto escogemos la subcategoria men 
    def subcategiria_men(self):
        return self.driver.find_element(By.XPATH, self.subcategoria).click()
    
    #con esto seleccionamos el primer elemento
    def selecion_primer_elemento(self):
        return self.driver.find_element(By.XPATH, self.primer_elemento).click()
    
    #con esto agregamos mas cantidad de un elemento al carrito 
    def agregar_mas_carrito(self):
        return self.driver.find_element(By.XPATH, self.agregar_carrito).click()
