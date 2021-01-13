import RPi.GPIO as gpio
import time
PIN=24
LED=21    
gpio.setmode(gpio.BCM) 
gpio.setwarnings(False)
gpio.setup(PIN, gpio.IN, pull_up_down = gpio.PUD_DOWN)
gpio.setup(LED, gpio.OUT)
estadoled = False
try:  ##posiblita parar o programa com CTRL + C
      ##precisa colcoar except KeyboardInterrupt:
      ##gpio.cleanup()
 while True:
  if gpio.input(PIN) == True:
     time.sleep(0.1)
     if estadoled == False: 
        gpio.output(LED, 1)
        estadoled = True
        time.sleep(0.10)
     else:
        gpio.output(LED,0)
        estadoled = False
        time.sleep(0.10)
except KeyboardInterrupt:
 gpio.cleanup()
 exit()
    