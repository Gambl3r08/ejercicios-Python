#Funciones en python
def dato (_nombre, _apellido):
    nombre_completo = _nombre, _apellido
    print(nombre_completo)

nombre = str(input("Ingrese su nombre: "))    
apellido = str(input("Ingrese su apellido: "))

_apellido = apellido
_nombre = nombre

dato(nombre, apellido)