from machine import Pin,UART 
import time

led_rouge = Pin(2, Pin.OUT)
led_vert = Pin(3, Pin.OUT)
led_bleu = Pin(4, Pin.OUT)
B1 = Pin(27, Pin.IN)
B2 = Pin(26, Pin.IN)
decompte = 0        # decompte vas de 0 a 2 pour allumer sucéssivement les leds

def test_button():  #fonction regarde si les bouton son activé
    valeurB1 = B1.value()
    valeurB2 = B2.value()
    if valeurB1:
        time.sleep_ms(500) #temps d'arret pour bouton (pour éviter que ca défile trop vitre)
    return valeurB1, valeurB2

def allume_led(decompte):   #fonction allume lumiere en fonction de décompte 0, 1, 2 crément a chaque chagement de led
    if decompte == 0:
        led_rouge.value(1)  # allume led rouge
        led_vert.value(0)
        led_bleu.value(0)
    if decompte == 1:
        led_rouge.value(0)
        led_vert.value(1)
        led_bleu.value(0)
    if decompte == 2:
        led_rouge.value(0)
        led_vert.value(0)
        led_bleu.value(1)
    decompte += 1
    if decompte > 2:
        decompte = 0
    return decompte

def eteind_led():     #éteint toutes les leds
    led_rouge.value(0)
    led_vert.value(0)
    led_bleu.value(0)
    return

while True:           #boucle sans fin du programe
    time.sleep_ms(50)  
    Bb1 = test_button()[0]
    Bb2 = test_button()[1]
    if Bb1 == True:
        decompte = allume_led(decompte)
        print('lo')
        
    if Bb2 == True:
        eteind_led()
        decompte = 0