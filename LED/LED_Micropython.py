import time
from machine import Pin
LED_PIN=Pin(5,Pin.OUT)        
while True:
  LED_PIN.value(1)            #Set led turn on
  time.sleep(0.5)
  LED_PIN.value(0)            #Set led turn off
  time.sleep(0.5)
