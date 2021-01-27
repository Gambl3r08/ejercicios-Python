# Usuario
print("ingrese su nombre de usuario")
usuario = input()
if usuario.isalpha() == True:
    while len(usuario) < 6:
        print("el usuario es menor a 6 caracteres")
        print("ingrese su nombre de usuario nuevamente")
        usuario = input()
    while len(usuario) > 12:
        print("el usuario excede los 12 caractere")
        print("ingrese su nombre de usuario nuevamente")
        usuario = input()
    else:
        print("El usuario tiene que tener letras y numeros")

# Contraseña
print("ingresa tu contraseña")
contra = input()

while len(contra) < 8:
    print("la contraseña tiene que tener minimo 8 caracteres")
    contra = input()

print("ingrese su usuario")
confir_usuario = input()

if usuario == confir_usuario:
    print("usuario correcto")


print("ingrese su contraseña")
confir_pass = input()

if contra == confir_pass:
    print("contraseña valida")