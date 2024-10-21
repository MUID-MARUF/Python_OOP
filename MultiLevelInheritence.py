#MultiLevel & Hierarchy Inheritence --->

class Human():
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def show(this):
    print("Name: ", this.name)
    print("Age: ", this.age)


class Male(Human):
  def __init__(self, name, age, gender):
    super().__init__(name, age)
    self.gender = gender

  def show(self):
    super().show()
    print("Gender: ", self.gender)


class Female(Human):
  def __init__(self, name, age, gender):
    super().__init__(name, age)
    self.gender = gender

  def show(self):
    super().show()
    print("Gender: ", self.gender)

class Army(Male):
  def __init__(self, name, age, gender, rank):
    super().__init__(name, age, gender)
    self.rank = rank

  def show(self):
      super().show()
      print("Rank: ", self.rank)


mili1 = Army("Muid", 23, "Male", "Captain")
mili1.show()