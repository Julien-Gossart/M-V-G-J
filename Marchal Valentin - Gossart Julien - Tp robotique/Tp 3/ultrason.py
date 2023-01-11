from hcsr04 import HCSR04 # inclu la librairie pour utiliser le capteur de distance à ultrasong
from machine import Pin, I2C # inclu la posibilitée des ce servir des pines I2C
from ssd1306 import SSD1306_I2C #inclu la librairie pour utiliser l'écrant au led
import time #inclu la librairie qui permet de mettre un délais

# réglage de l'écrant oled
pix_res_x  = 128 
pix_res_y = 64  

# Défini la fréquence de l'écrant oled ainci que les pines qui le relie au rasberry.
i2c_dev = I2C(0,scl=Pin(9),sda=Pin(8),freq=200000)

# Défini les pines auquel est relié le capteur de distance à ultrasong.
sensor = HCSR04(trigger_pin=1, echo_pin=0)

i2c_addr = [hex(ii) for ii in i2c_dev.scan()]

# Défini les réglages de l'écrant aux led ( largeur, hauteur, en nombre de pixel)
oled = SSD1306_I2C(pix_res_x, pix_res_y, i2c_dev)

while True:
    oled.fill(0) # on rempli l'écrant oled de rien, donc du noir.
    time.sleep_ms(50) # on met un délai de 50 ms
    distance = sensor.distance_cm()  # variable(la distance = valeur du capteur de distance)
    print('Distance:', distance, 'cm')
    oled.text("la distance est:",5,25) # affiche sur l'écrant "la distance est:", position x 5pixels, y 25 pixels
    oled.text(str(int(distance)),5,35) # affiche sur l'écrant "la distance est:", position x 5pixels, y 35 pixels
    oled.show()  # l'écrant oled affiche les variables qu'on luit a donné