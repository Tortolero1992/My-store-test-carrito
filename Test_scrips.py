import pytest
from test.test_page import inicio_secion

def Ejecucion_scrip():
    prueba = inicio_secion()
    prueba.inicio('tortolero1992@outlook.es','Prueba_123$')
    

def Test_ejecucion():
    assert Ejecucion_scrip()