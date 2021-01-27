# encoding latin1
import csv

def leer_datos(datos):
    try:
        return datos.next()
    except:
        return None


def ventas_clientes_mes(archivo_ventas):
    # inicializacion
    ventas = open(archivo_ventas)
    ventas_csv = csv.reader(ventas)

    item = leer_datos(ventas_csv)
    total = 0
    
    
    while item:
        cliente = item[0]
        total_cliente = 0
        print ("Cliente ", cliente)
	
	
        while item and item[0] == cliente and item[1] == anyo:
            mes, monto = item[2], float(item[3])
            print("Ventas del mes : ", mes, monto)
            total_anyo += monto

            item = leer_datos(ventas_csv)

        print("Total del año : ", anyo, total_anyo)
        total_cliente += total_anyo


    print ("Total para el cliente ", cliente, total_cliente)
    total += total_cliente

print("Total general: ", total)

ventas.close()

ventas_clientes_mes("ventas.csv")