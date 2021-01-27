# -*- coding: utf-8 -*-

def main():

    f = input("Cuanto cuesta un segundo de comunicacion ? ")
    n = input("Cuantas comunicaciones hubo? ")
    f = int (f)
    n = int (n)
    for x in range(n):
        hs = input("Cuantas horas? ")
        min = input("Cuantos minutos? ")
        seg = input("Cuantos segundos? ")

        segcalc = asegundos(hs, min, seg)

        costo = segcalc * f
        print("Duracion: ", segcalc, "Segundos. Costo: ", costo, " $")

def asegundos(horas, minutos, segundos):
    segsal = 3600 * horas + 60 * minutos + segundos
    return segsal

main()