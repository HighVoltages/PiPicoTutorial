import time
import board
import digitalio
LED_PIN = digitalio.DigitalInOut(board.GP5)
LED_PIN.direction = digitalio.Direction.OUTPUT
while True:
    LED_PIN.value = True
    time.sleep(0.5)
    LED_PIN.value = False
    time.sleep(0.5)
