# rename this code.py on the CPE to run
import time
import board
import analogio

MAXREAD = 65520  # this is max reading on ADC

analogin = analogio.AnalogIn(board.A6)


def getValue(pin):  # helper
    raw = pin.value
    value = (raw * 255 / MAXREAD) # returns value between 0 and 255
    return (value)

while True:
    print("Normalized value: %i" % getValue(analogin))
    time.sleep(0.5)
