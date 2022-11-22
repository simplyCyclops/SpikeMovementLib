from math import *
import time

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

generator = linear_generator(0.1)
res = set()
for i in generator:
  res.add(i)

print(sorted(list(res)))