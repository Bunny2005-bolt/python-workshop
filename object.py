#creating a object
class Dog:
    def __init__(self,name):
        self.name=name
dog1=Dog("buddy")
print(dog1.name)

#creating a class
class car:
    def __init__(self, make,model):
        self.make=make
        self.model=model

car1=car("toyota","honda")
car2=car("civic","caary")

print(car1.make,car1.model)
print(car2.make,car2.model)


