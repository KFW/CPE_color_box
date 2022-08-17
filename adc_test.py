# rename this code.py on the CPE to run
import time
import board
import analogio

analogin = analogio.AnalogIn(board.A6)


def getVoltage(pin):  # helper
    return (pin.value * 3.3) / 65536


while True:
    print("Analog Voltage: %f" % getVoltage(analogin))
    time.sleep(0.1)