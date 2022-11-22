import interpolation

class MotorPair: # dummy class
  def start_tank_at_power(l, r): pass
  def start_at_power(p): pass
  def stop(): pass

class Chassis(MotorPair):
  def __init__(self, l_port, r_port, wheel_circ):
    self.l_port = l_port
    self.r_port = r_port
    self.wheel_circ = wheel_circ

    self.l_wheel = None
    self.r_wheel = None
  
  def deg_to_cm(self, deg):
    return deg/360 * self .wheel_circ

  def cm_to_deg(self, cm):
    return cm/self .wheel_circ * 360

  def distance_traveled(self):
    deg_traveled = (self.l_wheel.get_degrees_counted() + self.r_wheel.get_degrees_counted())/2
    return self.deg_to_cm(deg_traveled)

  def move(self, l_speed, r_speed, distance, acc_time=1):
    # TODO: reset taco count

    speed_ratio = l_speed / r_speed
    lsp = l_speed
    rsp = r_speed

    for i in interpolation.linear(acc_time):
      self.start_tank_at_power(i*l_speed, i*r_speed)
    
    while self.distance_traveled() < distance:
      l_deg = self.l_wheel.get_degrees_counted()
      r_deg = self.r_wheel.get_degrees_counted()
      ratio = l_deg / r_deg

      if ratio > speed_ratio:
        rsp = r_speed * ratio
      elif ratio < speed_ratio:
        lsp = l_speed * (1/ratio)

    for i in interpolation.linear(acc_time):
      j = 1-i
      self.start_tank_at_power(j*l_speed, j*r_speed)

    self.stop()