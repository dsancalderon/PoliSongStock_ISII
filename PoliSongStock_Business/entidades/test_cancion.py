import pytest

from cancion import Cancion   
def test_mostrar_detalle():
    # Arrange: crear objeto de prueba
    cancion = Cancion(
        id=1,
        nombre="Shape of You",
        artista="Ed Sheeran",
        precio=3.50,
        duracion=4.24,
        tamano_kb=4500,
        calidad="Alta"
    )

    # Act: ejecutar el método
    resultado = cancion.mostrar_detalle()

    # Assert: comparar con el resultado esperado
    assert resultado == "Shape of You - Ed Sheeran (4.24 min) - $3.50"