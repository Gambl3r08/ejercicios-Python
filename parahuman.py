# parahumanos.py
#!/usr/bin/python
# -*- coding: utf-8 -*-

SUFIJOS = {1000: [ 'KB' , 'MB' , 'GB' , 'TB' , 'PB' , 'EB' , 'ZB' , 'YB' ] ,
           1024: [ 'KiB ' , 'MiB ' , 'GiB ' , 'TiB ' , 'PiB ' , 'EiB ' , ' ZiB ' ,
                   'YiB ' ]}
 
def tamanyo_aproximado(tamanyo , un_kilobyte_es_1024_bytes=True ):
    ''' Convierte un tamaño de fichero en formato legible por personas
 
     Argumentos/parámetros:
     tamanyo __ tamaño de fichero en bytes
     un_kilobyte_es_1024_bytes __ si True (por defecto),
                                  usa múltiplos de 1024
                                  si False, usa múltiplos de 1000

     retorna : string
 
     '''    
 
    if tamanyo < 0 :
        raise ValueError ("el número debe ser no negativo")
 
    multiplo = 1024 if un_kilobyte_es_1024_bytes else 1000
    for sufijo in SUFIJOS [multiplo]:
        tamanyo /= multiplo
        if tamanyo < multiplo:
            return ' {0:.1f} {1} ' . format ( tamanyo , sufijo)
 
    raise ValueError ( 'número demasiado grande ' )
 
if __name__ == '__ main__':
    print (tamanyo_aproximado (1000000000000 , False))
    print (tamanyo_aproximado (1000000000000) )