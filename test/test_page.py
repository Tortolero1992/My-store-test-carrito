import time
from PageObject.home_page import home_page

#creamos la claseque ejecutara la prueba 
class inicio_secion:
    
    def inicio (self, usuario, contraseña):
       
        inicio = home_page()
        inicio.webDriverGet()
        inicio.iniciar_secion()
        time.sleep(2)
        inicio.cuadro_correo(usuario)
        inicio.cuadro_pass(contraseña)
        inicio.iniciar_secion_enter()
        time.sleep(2)
        inicio.categoria_clothes()
        inicio.subcategiria_men()
        time.sleep(2)
        inicio.selecion_primer_elemento()
        inicio.agregar_mas_cantidad()
        time.sleep(2)
        inicio.agregar_mas_carrito()
        time.sleep(5)


