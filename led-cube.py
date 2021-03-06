import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

APIN = [14, 15, 18, 11, 9, 10, 5, 6, 13]
CPIN = [21, 20, 16]

for i in APIN:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, GPIO.LOW)

for i in CPIN:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, GPIO.HIGH)

SLEEP_LEN = 0.0008
ACTIONS = [(300, 0b111111111, 0b111111111, 0b111111111),
           ( 50, 0b111111111, 0b000000000, 0b000000000),
           ( 50, 0b000000000, 0b111111111, 0b000000000),
           ( 50, 0b000000000, 0b000000000, 0b111111111),
           ( 50, 0b000000000, 0b111111111, 0b000000000),
           ( 50, 0b111111111, 0b000000000, 0b000000000),
           ( 50, 0b000000000, 0b111111111, 0b000000000),
           ( 50, 0b000000000, 0b000000000, 0b111111111),
           ( 50, 0b000000000, 0b111111111, 0b000000000),
           ( 50, 0b111111111, 0b000000000, 0b000000000),
           ( 50, 0b000000000, 0b111111111, 0b000000000),
           ( 50, 0b000000000, 0b000000000, 0b111111111),
           ( 50, 0b000000000, 0b111111111, 0b000000000),
           ( 50, 0b111111111, 0b000000000, 0b000000000),
           ( 50, 0b100000000, 0b100000000, 0b100000000),
           ( 50, 0b010000000, 0b010000000, 0b010000000),
           ( 50, 0b001000000, 0b001000000, 0b001000000),
           ( 50, 0b000001000, 0b000001000, 0b000001000),
           ( 50, 0b000000001, 0b000000001, 0b000000001),
           ( 50, 0b000000010, 0b000000010, 0b000000010),
           ( 50, 0b000000100, 0b000000100, 0b000000100),
           ( 50, 0b000100000, 0b000100000, 0b000100000),
           ( 50, 0b100000000, 0b100000000, 0b100000000),
           ( 50, 0b010000000, 0b010000000, 0b010000000),
           ( 50, 0b001000000, 0b001000000, 0b001000000),
           ( 50, 0b000001000, 0b000001000, 0b000001000),
           ( 50, 0b000000001, 0b000000001, 0b000000001),
           ( 50, 0b000000010, 0b000000010, 0b000000010),
           ( 50, 0b000000100, 0b000000100, 0b000000100),
           ( 50, 0b000100000, 0b000100000, 0b000100000),
           ( 25, 0b100000000, 0b000000000, 0b000000000),
           ( 25, 0b010000000, 0b000000000, 0b000000000),
           ( 25, 0b001000000, 0b000000000, 0b000000000),
           ( 25, 0b000001000, 0b000000000, 0b000000000),
           ( 25, 0b000010000, 0b000000000, 0b000000000),
           ( 25, 0b000100000, 0b000000000, 0b000000000),
           ( 25, 0b000000100, 0b000000000, 0b000000000),
           ( 25, 0b000000010, 0b000000000, 0b000000000),
           ( 25, 0b000000001, 0b000000000, 0b000000000),
           ( 25, 0b000000000, 0b000000001, 0b000000000),
           ( 25, 0b000000000, 0b000000010, 0b000000000),
           ( 25, 0b000000000, 0b000000100, 0b000000000),
           ( 25, 0b000000000, 0b000100000, 0b000000000),
           ( 25, 0b000000000, 0b000010000, 0b000000000),
           ( 25, 0b000000000, 0b000001000, 0b000000000),
           ( 25, 0b000000000, 0b001000000, 0b000000000),
           ( 25, 0b000000000, 0b010000000, 0b000000000),
           ( 25, 0b000000000, 0b100000000, 0b000000000),
           ( 25, 0b000000000, 0b000000000, 0b100000000),
           ( 25, 0b000000000, 0b000000000, 0b010000000),
           ( 25, 0b000000000, 0b000000000, 0b001000000),
           ( 25, 0b000000000, 0b000000000, 0b000001000),
           ( 25, 0b000000000, 0b000000000, 0b000010000),
           ( 25, 0b000000000, 0b000000000, 0b000100000),
           ( 25, 0b000000000, 0b000000000, 0b000000100),
           ( 25, 0b000000000, 0b000000000, 0b000000010),
           ( 25, 0b000000000, 0b000000000, 0b000000001),
           ( 50, 0b000000000, 0b000000000, 0b000000001),
           ]

actIdx = 0
tick = 0
outputPin = GPIO.LOW

try:
    while True:
        if tick >= ACTIONS[actIdx][0]:
            actIdx += 1
            tick = 0
            if actIdx >= len(ACTIONS):
                actIdx = 0
        
        action = ACTIONS[actIdx]

        GPIO.output(CPIN[0], GPIO.LOW)
        flag = action[1]
        for k, v in enumerate(APIN):
            if ((flag >> (8 - k)) & 0b1) == 1:
                outputPin = GPIO.HIGH
            else:
                outputPin = GPIO.LOW
            GPIO.output(v, outputPin)
        sleep(SLEEP_LEN)
        GPIO.output(CPIN[0], GPIO.HIGH)

        GPIO.output(CPIN[1], GPIO.LOW)
        flag = action[2]
        for k, v in enumerate(APIN):
            if ((flag >> (8 - k)) & 0b1) == 1:
                outputPin = GPIO.HIGH
            else:
                outputPin = GPIO.LOW
            GPIO.output(v, outputPin)
        sleep(SLEEP_LEN)
        GPIO.output(CPIN[1], GPIO.HIGH)

        GPIO.output(CPIN[2], GPIO.LOW)
        flag = action[3]
        for k, v in enumerate(APIN):
            if ((flag >> (8 - k)) & 0b1) == 1:
                outputPin = GPIO.HIGH
            else:
                outputPin = GPIO.LOW
            GPIO.output(v, outputPin)
        sleep(SLEEP_LEN)
        GPIO.output(CPIN[2], GPIO.HIGH)

        tick += 1

except KeyboardInterrupt:
    GPIO.cleanup()


