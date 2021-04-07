"""
Escribir una función diasiguiente(…) que reciba como parámetro una fecha cualquiera expresada por tres enteros
(correspondientes al día, mes y año) y calcule y
devuelva tres enteros correspondientes el día siguiente al dado.
Utilizando esta función, desarrollar programas que permitan:
a. Sumar N días a una fecha.
b. Calcular la cantidad de días existentes entre dos fechas cualesquiera.
"""

def verificar_fecha(dia,mes):
    while dia<1 or dia >31 :
        print("dia invalido")
        dia=int(input("ingrese una dia valido: "))
    while mes<1 or mes>12:
        print("mes invalido")
        mes=int(input("ingrese mes valido: "))
    return dia,mes


def sumardia(dia,mes,year):
    
    dia, mes = verificar_fecha(dia, mes)
    dia+=1
    if dia>31:
        dia=1
        mes=mes+1
        if mes>12:
            mes=1
            year=year+1
    return dia, mes, year

def calcular_dias(dia,mes,year):
    pass


dia=int(input(" dia: "))
mes=int(input(" mes: "))
year=int(input("year: "))

#dia,mes=verificar_fecha(dia,mes)

#print(f"la fecha es dia: {dia} del mes: {mes}")

d,m,a=sumardia(dia,mes,year)
print("dia: ",d,"mes: ",m,"year: ",a)