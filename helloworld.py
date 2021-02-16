import machine
import utime

led_onboard = machine.Pin(15, machine.Pin.OUT)

while True:
    led_onboard.toggle()
    utime.sleep(10)
