class Car():
  def __init__(self, name, model, color, sellingDate):
    self.name = name
    self.model = model
    self.color = color
    self.sellingDate = sellingDate

  def show(self):
    print("Car Name: ", self.name)
    print("Car Model: ", self.model)
    print("Car Color: ", self.color)
    print("Car sold : ", self.sellingDate)
    print("\n")

  def updateColor(self, newColor):
    self.color = newColor
    print("Color Updated Succesfully !!")

  def updateSellingDate(self, newSellingDate):
    self.sellingDate = newSellingDate
    print("Selling Date Updated Succesfully !!")

car1 = Car("Toyota", "Corolla", "Black", "August 2020")
car1.show()
car1.updateColor("Red")
car1.show()
car1.updateSellingDate("October 2020")
car1.show()