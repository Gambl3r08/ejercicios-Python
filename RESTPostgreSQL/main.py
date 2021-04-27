from DBManejador import *
from ManejadorArchivos import *

def ciclo():
    print("Pulse Ctrl + C para detener")
    while(true):
        lecturaBt = ""
        if lecturaBt != "":
            AgregarDato(cursor, lecturaBt)
            lecturaBt = ""
        else:
            continue



# Conectando a la DB y creando cursor para recorrerla
dbconnect = ConectarDB()
cursor = CrearCursor(dbconnect)

# Agregando dato
#dato = "2222 5555 4444 230 8888 231111"
#gregarDato(cursor, dato)

#print(ConsultarTodo(cursor))
#listaDatos = ConsultarTodo(cursor)
#EscribirArchivo('datosDB.ods', listaDatos)




# Cerrando la conexión
CerrarConexion(dbconnect)



