from machine import Pin, PWM
from time import sleep

red = PWM(Pin(15))
green = PWM(Pin(16))
blue = PWM(Pin(17))

red.freq(1000)
green.freq(1000)
blue.freq(1000)

def set_color(r, g, b):
    red.duty(r)
    green.duty(g)
    blue.duty(b)

while True:
    set_color(1023, 0, 0)
    sleep(1)
    set_color(0, 1023, 0)
    sleep(1)
    set_color(0, 0, 1023)
    sleep(1)
    set_color(1023, 1023, 0)
    sleep(1)
