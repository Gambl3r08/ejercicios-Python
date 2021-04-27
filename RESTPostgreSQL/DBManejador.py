import sys
import psycopg2
from ManejadorArchivos import *

def ConectarDB():
    try:
        conexion = psycopg2.connect(host="localhost", database="postgres", user="postgres", password="postgres")
        print("conexión establecida")
        return conexion
    except:
        print("Error al conectar al DB")
        print("Unexpected error:", sys.exc_info()[0])
        raise

def CerrarConexion(conexion):
    try:
        conexion.close()
    except:
        print("Error al cerrar la conexion")
        print("Unexpected error:", sys.exc_info()[0])
        raise


def CrearCursor(conexion):
    try:
        cur = conexion.cursor()
        return cur
    except:
        print("No se puedo crear un cursos")
        print("Unexpected error:", sys.exc_info()[0])
        raise


def ConsultarTodo(cur):
    try:
         cur.execute("SELECT * FROM public.lecturas") 
         listaDatos = []
         for dato in cur.fetchall():
             listaDatos.append(dato)
         return listaDatos
    
    except:
        print("no se puedo generar la consulta")
        print("Unexpected error:", sys.exc_info()[0])
        raise


def AgregarDato(cur, cadena):
    try:
        listaParametros = cadena.split()
        print("Lista Datos a insertar: ", listaParametros)
        cur.execute("INSERT INTO lecturas VALUES ("+"localtimestamp"+","+listaParametros[0]+","+listaParametros[1]+","+listaParametros[2]+","+listaParametros[3]+","+listaParametros[4]+","+listaParametros[5]+")")
        print("Dato insertado")
    
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise





#dbconnect = ConectarDB()
#cursor = CrearCursor(dbconnect)

#listaDatos = ConsultarTodo(cursor)
#CerrarConexion(dbconnect)
#EscribirArchivo('datosDB.ods', listaDatos)
#.ods
#.txt
