paquete = 'sudo pacman -S codeblocks'
rsi = 'y'
rno = 'n'

sudo = str(input(' [root] $  '))
if sudo == paquete:
    r = str(input('ingrese y para continuar o n para finalizar  '))
    
elif r == rsi:
    print("Compilacion terminada con exito ")    
elif r == rno:
    print("Compilacion cancelada. ")    


input(" Precione cualquier tecla para finalizar ")    