import RPi.GPIO as gpio
import time
 
""" Global """
PIN=24
LED=21
""" Funcoes """
def action_press_button(gpio_pin):
      gpio.output(LED,1)

 
""" Configurando GPIO """
# Configurando o modo dos pinos como BCM
gpio.setmode(gpio.BCM) 
gpio.setwarnings(False)
# Configurando PIN como INPUT e modo pull-donw interno
gpio.setup(PIN, gpio.IN, pull_up_down = gpio.PUD_DOWN)
gpio.setup(LED, gpio.OUT)
#adicionando evento
gpio.add_event_detect(PIN, gpio.RISING)
while True:
    if gpio.event_detected(PIN):
        action_press_button(PIN)
    time.sleep(1)
gpio.cleanup()
exit()
    