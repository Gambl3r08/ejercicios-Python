#!/usr/bin/python

import socket

s = socket.socket()
host = socket.gethostname()
port = 12221

s.connect((host, port))
print("Connected to", host)

while True:
    z = input("ingresa algo al servidor: ")
    s.send(z)
    # Haltz
    print("Esperando respuesta...")
    print(s.recv(1024))