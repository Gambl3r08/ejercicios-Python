# Pasar palabras en ingles de Singular a plural
import re

def plural(nombre):
    if re.search('[sxz]$', nombre):
        return re.sub('$', 'es', nombre)
    elif re.search('[^aeioudgkprt]h$', nombre):
        return re.sub('$', 'es', nombre)
    elif re.seatch('[^aeiou]y$', nombre):
        return re.sub('y$', 'ies', nombre)
    else:
        return nombre + 's'