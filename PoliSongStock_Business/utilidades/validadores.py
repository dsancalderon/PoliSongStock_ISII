import re

def validar_correo(email: str) -> bool:
    return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None

def validar_precio(precio: float) -> bool:
    return precio > 0
