import time

E9 = 10**9

def __interpolator(duration, func):
  duration *= E9
  i = 0
  start_time = time.time_ns()

  while i < 1:
      yield i
      i = func((time.time_ns()-start_time)/duration)
  yield 1

def linear(duration):
  return __interpolator(duration, lambda x: x)

def exponential(duration, intensity = 10):
  if intensity <= 1: 
    raise AttributeError(f"exponential intensity must be bigger than 1! (is {intensity})")

  func = lambda x: (intensity**x - 1)/(intensity-1)

  return __interpolator(duration, func)