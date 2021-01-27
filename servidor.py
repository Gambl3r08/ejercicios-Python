#!/usr/bin/python

import socket

s = socket.socket()
host = socket.gethostname()
port = 12221
s.bind((host, port))

s.listen(5)
c = None

while True:
    if c is None:
        # Halts
        print("[Esperando la coneccion]")
        c, addr = s.accept()
        print("Enviando coneccion a: ", addr)
    else:
        # Halts
        print("[Esperando la respuesta...]")
        print(c.recv(1024))
        q = input("Ingresa algo al cliente: ")
        c.send(q)