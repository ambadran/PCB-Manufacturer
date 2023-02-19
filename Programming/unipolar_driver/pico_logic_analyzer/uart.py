import time
from machine import Pin, UART

uart = UART(0, baudrate=1200, tx=Pin(0), rx=Pin(1))

def get_num():
    test = uart.read()
    try:
        return test[1]<<8 | test[0]
    except Exception: 
        return None


while True:
    print(get_num())
    time.sleep(0.05)
