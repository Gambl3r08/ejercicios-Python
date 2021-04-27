# Leer y escribir archivos en diferentes formatos
import os
import sys

def LeerArchivo(nombre):
    try:
        actualPath = os.getcwd() + '/' + nombre
        archivo = open(actualPath, 'r')
        listaDatos = []
        
        for i in archivo:
            i = i.replace('\n', '')
            #i = i.split('|')
            i = i.replace('|', '')
            #print(i)
            listaDatos.append(i)
        
        archivo.close()
        return  listaDatos
    except:
        print("error al abrir el archivo")


def EscribirArchivo(nombre, lista):
    try:
        archivo = open(nombre, "a")
        cont = 1
        if cont == 0:
            archivo.write("FECHA, O3 ,CO2 ,PM10 ,CO ,TEMP ,HUMED\n")
            cont = 1
        
        for i in lista:
            #i = str(i[0])+ str(i[1]) + str(i[2])+str(i[3])+str(i[4])+str(i[5])+str(i[6])
            archivo.write(str(i[0]))
            archivo.write(','+str(i[1]))
            archivo.write(','+str(i[2]))
            archivo.write(','+str(i[3]))
            archivo.write(','+str(i[4]))
            archivo.write(','+str(i[5]))
            archivo.write(','+str(i[6]+'\n'))
            
            i = str(i).replace('(', '')
            i = str(i).replace(')', '')
            i = str(i) +'\n'
            
            #archivo.write(str(i))
        archivo.close()
        print("Archivo creado correctamente")
    
    except:
        print("no se puedo escribir")
        print("Unexpected error:", sys.exc_info()[0])
        raise