#Multiple Inheritence --->

class Phone():
  def __init__(self, name, speed):
    self.name = name
    self.speed = speed 

  def show(self):
    print("Name: ", self.name)
    print("Speed: ", self.speed)

class Camera():
  def __init__(self,name, size):
    self.name = name
    self.size = size

  def show(self):
    print("Name: ", self.name)
    print("Size: ", self.size)

class SmartPhone(Phone, Camera):
  def __init__(self, name, speed, size):
    Phone.__init__(self, name, speed)
    Camera.__init__(self, name, size)

  def show(self):
    print("Phone Name: ", self.name)
    print("Phone Speed: ", self.speed)
    print("Camera Size: ", self.size)

smp1 = SmartPhone("iPhone 16", "5G", "48MP")
smp1.show()