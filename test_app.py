import pytest
from app import app

# Configuramos un cliente de pruebas para simular peticiones sin prender el servidor real
@pytest.fixture
def cliente():
    app.config['TESTING'] = True
    with app.test_client() as cliente:
        yield cliente

def test_inicio(cliente):
    """Prueba que la ruta principal responda correctamente"""
    respuesta = cliente.get('/')
    assert respuesta.status_code == 200
    assert b"exitoso" in respuesta.data

def test_saludo_valido(cliente):
    """Prueba que un nombre normal sea aceptado"""
    respuesta = cliente.get('/saludo/Luz')
    assert respuesta.status_code == 200
    assert b"Hola, Luz" in respuesta.data

def test_saludo_largo_seguridad(cliente):
    """Prueba que la seguridad de la Parte D funcione (bloquear nombres de más de 20 caracteres)"""
    respuesta = cliente.get('/saludo/EsteNombreEsDemasiadoLargoYDebeFallar')
    assert respuesta.status_code == 400  # 400 significa "Bad Request"
