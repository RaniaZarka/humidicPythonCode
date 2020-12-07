BROADCAST_TO_PORT = 12345
import time
from socket import *
from sense_hat import SenseHat
from datetime import datetime
from time import sleep
from csv import writer

sense = SenseHat()

#pressure = sense.get_pressure()
red = (255, 0, 0)

s = socket(AF_INET, SOCK_DGRAM)
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
    
while True:
    data = int(sense.get_humidity())
    data = str(data)
    s.sendto(bytes(data, "UTF-8"), ('<broadcast>', BROADCAST_TO_PORT))
    print(data)
    
    sense.show_message(str(data), text_colour=red, scroll_speed=0.02)
    sleep(2)
        
