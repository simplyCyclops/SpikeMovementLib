from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from math import *
import time

WHEEL_CIRC = 2.4 #FIX

hub = PrimeHub()

hub.light_matrix.show_image('HAPPY')

l_wheel = Motor('B')
r_wheel = Motor('C')
chassis = MotorPair('B', 'C')

def linear_generator(duration):
    duration *= 10**9
    i: float = 0
    start_time = time.time_ns()
    while i < 1:
        yield i
        i = (time.time_ns()-start_time)/duration
    yield 1

def accelerate(duration, invert = False):
    generator = linear_generator(duration)

    get_power = (lambda x: 100 * x) if not invert else (lambda x: 100 - 100 * x)
    for speed in generator:
        chassis.start_at_power(int(get_power(speed)))

def deg_to_cm(self, deg):
    return deg/360 * WHEEL_CIRC

def distance_traveled(self):
  deg_traveled = (self.l_wheel.get_degrees_counted() + self.r_wheel.get_degrees_counted())/2
  return self.deg_to_cm(deg_traveled)

def move(speed, distance, acc_time=1):
  l_wheel.reset_degrees_counted() # fix please
  r_wheel.reset_degrees_counted() # fix please

  lsp = speed
  rsp = speed

  accelerate(acc_time)
  while distance_traveled() < distance:
        l_deg = l_wheel.get_degrees_counted()
        r_deg = r_wheel.get_degrees_counted()
        ratio = l_deg / r_deg

        if ratio > 1:
          rsp = speed * ratio
        elif ratio < 1:
          lsp = speed * (1/ratio)
        
        chassis.start_tank_at_power(lsp, rsp)

  accelerate(acc_time, invert=True)
  chassis.stop()

# START
move(30, 30)