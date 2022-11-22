from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from math import *

import time

hub = PrimeHub()

hub.light_matrix.show_image('HAPPY')

motor = Motor('A')

def linear_generator(duration):
    duration *= 10**9
    i: float = 0
    start_time = time.time_ns()
    while i < 1:
        yield i
        i = (time.time_ns()-start_time)/duration
    yield 1

def accelerate(duration, motor, invert = False):
    generator = linear_generator(duration)

    get_power = (lambda x: 100 * x) if not invert else (lambda x: 100 - 100 * x)
    for speed in generator:
        motor.start_at_power(int(get_power(speed)))

accelerate(2, motor)
wait_for_seconds(3)
generator = linear_generator(2)
accelerate(2, motor, invert=True)
motor.stop()