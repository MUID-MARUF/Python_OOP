class Student():
    def __init__(self,name, id, hometown):
        self.name = name
        self.id = id
        self.hometown = hometown

    def show(self):
        print(f"His name is {self.name}")
        print(f"His id is {self.id}")
        print(f"His hometown is {self.hometown}")

ob1 = Student("Muid", 1237, "Manikganj")
ob1.show()