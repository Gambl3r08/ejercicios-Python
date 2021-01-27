def es_palindromo(frase):
    std = str(frase).lower().replace(' ', '')
    return std == std[::-1]



f = "yo hago yoga hoy"
resultado = es_palindromo(f)
print(resultado)