from machine import Pin
import network
import socket
from time import sleep
# from picozero import pico_temp_sensor, pico_led
import machine

led = Pin('LED', Pin.OUT)

ssid = "Mr.A's Lab"
password = "lskdmin2938#$"

def connect():
    #Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        sleep(1)
    ip = wlan.ifconfig()[0]
    print(f'Connected on {ip}')
    return ip


def open_socket(ip):
    # Open a socket
    address = (ip, 1234)
    connection = socket.socket()
    connection.bind(address)
    connection.listen(1)
    print(connection, 'connection')
    return connection


def serve(connection):
    #Start a web server
    # state = 'OFF'
    # pico_led.off()
    # temperature = 0
    client = connection.accept()[0]
    while True:
        request = client.recv(1024)
        request = str(request)

        request = request.strip()
        print(request, 'from tcp socket')

        to_be_sent = request + ' from pico\n'
        client.send(to_be_sent)
        # client.close()


def start():
    try:
        ip = connect()
        connection = open_socket(ip)
        serve(connection)
    except KeyboardInterrupt:
        machine.reset()

