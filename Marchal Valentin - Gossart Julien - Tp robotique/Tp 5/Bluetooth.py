from machine import UART, Pin #import l'utilisation des pines UART
import time #import une librairie nous permettant d'utiliser une fonction mettant du délait
import json 

# défini (leur emplacements, le temps de rafraichissement des pines UART, la position du TX et RX) . 
uart1 = UART(0, baudrate = 38400, tx= Pin(0), rx=Pin(1)) 

while (True):
    uart1.write('salut')  # on revoie "salut" au module breuthoot raccordé pour qu'il envoie le message
    print(uart1.read(5)) # on écrit l'information envoyée 
    if uart1.any() > 0: # on regarde si on a recu une quelconque réponce  
        strBT = str(uart1.readline(),"utf-8") # crée une variable str( qui équiveau au message recu)
        print(strBT) # on print la variable
        strSplit = strBT.split(";") # on recoit un string séparé par ; 
        print(strSplit[0]) 
        for x in range(len(strSplit)): # on affiche tout les mots contenu dans la suite
            print(strSplit[x])
    time.sleep(1) # latence de 1 ms
