"""
Escribir un programa que permita grabar un archivo los datos de lluvia caída durante un año.
Cada línea del archivo se grabará con el siguiente formato:
<dia>;<mes>;<lluvia caída en mm> por ejemplo 25;5;319
Los datos se generarán mediante números al azar, asegurándose que las fechas
sean válidas. La cantidad de registros también será un número al azar entre 50 y
200. Por último se solicita leer el archivo generado e imprimir un informe en formato matricial donde
cada columna represente a un mes y cada fila corresponda a
los días del mes. Imprimir además el total de lluvia caída en todo el año.
"""
import random


def fecha(dia,mes):
    
    if dia<=31 and mes<=12:
        
        return True
    if mes==2 and dia>29:
        return False
    
        
def archivo():
    try:
        archivo=open("ejercicio 2.txt","wt")
        registros=random.randint(5,10)
        cont=0
        while cont<registros:
            dia=random.randint(1,30)
            mes=random.randint(1,12)
            lluvia=random.randint(100,900)
            
            archivo.write(str(dia)+";"+str(mes)+";"+str(lluvia)+"\n")
            cont+=1
        print("archivo cargado correctamente")
    
    except FileNotFoundError as mensaje:
        print("no se puede crear archivo correctamente",mensaje)
    except OSError:
        print("error")
        
    finally:
        try:
            arch.close()
        except NameError:
            pass

            
            
        


dia=random.randint(1,31)
mes=random.randint(1,12)
fecha=fecha(dia,mes)
print(fecha)

archivo()