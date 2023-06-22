import time
from machine import Pin, UART

uart = UART(1, baudrate=1200, tx=Pin(4), rx=Pin(5))


def print_output_specific():
    '''
    whenever start character is detected, it's assumed that OF_num_TMR1 and target_OF_num is sent each as a 16-bit value
    '''
    while uart.read(1)[0] != 0x0:
        pass
    
    res = uart.read(6)
    print(f"OF_num_TMR1: {res[1]<<8 | res[0]}, target_OF_num: {res[3]<<8 | res[2]}, current_pos: {res[5]<<8 | res[4]}  \r", end='')

def print2():
    '''
    v2
    '''
    # while chr(uart.read(1)[0]) != '\n':
    #     pass

    # res = uart.read(19)
    res = uart.readline()
    print(res[8], end='\r')
    # try:
    #     print(res.decode()[8], end='\r')
    # except Exception:
    #     pass

def main():
    while True:
        print2()
        time.sleep(0.2)

def main2():
    while True:
        print('value: ', int(uart.read(1)[0]), end='\r');
        time.sleep(0.2)
