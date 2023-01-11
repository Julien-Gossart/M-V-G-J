from machine import Pin, UART, PWM, ADC #importe tous les types de fonction qu'on a besoin
from ssd1306 import SSD1306_I2C
import time

ENA = PWM(Pin(0)) # modulation de la largeur d'impulsion
ENA.freq(2000)
IN1 = Pin(1, Pin.OUT)
IN2 = Pin(2, Pin.OUT)

Vrx = ADC(Pin(26)) # valeur analogique de l'axe x 
Vry = ADC(Pin(27)) # valeur analogique de l'axe y

def scale_value (value,in_min,in_max,out_min,out_max): # fonction qui traduit les valeurs de sortie du joystick en pourcentage
    scaled_value = (value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min 
    return scaled_value

while True:
    
    val_y = Vry.read_u16() # lecture et écriture de la valeur du joystick dans une variable 
    val_x = Vrx.read_u16()
    
    print(val_y)
    time.sleep_ms(200) # utilisé pour avoir le temps (ms) de lire les valeurs

    if val_y <= 45000:
        ENA.duty_u16((-val_y)+65000) # modifie la vitesse du moteur (sens horloger)
        IN1.value(1)
        IN2.value(0)
        print(int(scale_value(y_value,0,45000,0,100))) # affichage du pourcentage 

    elif val_y >= 55000:
        ENA.duty_u16(val_y) # modifie la vitesse du moteur (sens anti-horloger)  
        IN1.value(0)
        IN2.value(1)
        print(int(scale_value(y_value,50000,65535,0,100))) # affichage du pourcentage 
        
    else:
        IN1.value(0) #arrêt du moteur
        IN2.value(0)
        
while True:
    oled.fill(o)
    time.sleep_ms(50)
    oled.text(str(int(scale_value(y_value,0,45000,0,100))),5,25)
    oled.show()