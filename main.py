import machine
import utime


led = machine.PWM(machine.Pin(15, machine.Pin.OUT))
led.freq(1000)

button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

pressCount = 0


def blink(count):
    if (count == 0):
        return

    led.duty_u16(5000)
    utime.sleep_ms(150)
    led.duty_u16(50)
    utime.sleep_ms(150)
    blink(count - 1)


while True:
    if button.value() == 1:
        print("pressed!!")
        pressCount += 1
        utime.sleep_ms(500)
        blink(pressCount)
