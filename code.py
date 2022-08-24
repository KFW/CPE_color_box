#control color of neopixels on Circuit Playground Express with rheostats.
import time
import board
import analogio
import neopixel

MAXREAD = 65520  # this is max reading on ADC

rpin = analogio.AnalogIn(board.A3)
gpin = analogio.AnalogIn(board.A4)
bpin = analogio.AnalogIn(board.A7)
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=1, auto_write=False)

def getValues(rpin, gpin, bpin):  # helper
    r_raw = rpin.value
    g_raw = gpin.value
    b_raw = bpin.value
    rval = r_raw * 255 // MAXREAD   # returns int value between 0 and 255
    gval = g_raw * 255 // MAXREAD
    bval = b_raw * 255 // MAXREAD 
    return (rval, gval, bval)

while True:
    R, G, B = getValues(rpin, gpin, bpin)
    print(R, G, B)
    pixels.fill((R,G,B))
    pixels.show()
    time.sleep(0.1)
