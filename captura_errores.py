# -*- coding: utf-8 -*-

import pdb

from subprocess import call, Popen, PIPE

# Limpiar pantalla
call("clear")

pdb.Pdb().set_trace()
proceso = Popen(['ls', '-lha'], stdout=PIPE, stderr=PIPE)
error_encontrado = proceso.stderr.read()
proceso.stderr.close()
listado = proceso.stdout.read()

proceso.stdout.close()


if not error_encontrado:
    print (listado)
else:
    print("se produjo el siguente error:\n%s" %error_encontrado)