
# 1)

### CLASSES ###

class car: 
    #constructor 
    def __init__(self, make, model, color="blue"):
        #attributes 
        self.wheels = 4
        self.make = make
        self.model = model
        self.color = color
        self.speed = 0 
    
    def set_color(self, color):
        self.color = color

    def accelerate(self, speed):
        self.speed += speed

    def sit_in_sun(self):
        self.set_color("white")

    def crash(self, other):
        self.wheels = 0
        other.wheels = 0
        self.speed = 0
        other.speed = 0

a = car("Toyota", "RAV4")

a.set_color("green")

a.sit_in_sun()

print(a.color)

b = car("Tesla", "Model 3")

a.crash(b)

print(a.wheels)

print(b.wheels)


### REFERENCES ### (define 'None')



### PASS BY REFERENCE VS PASS BY VALUE ###


# 2)

### INTERFACES ###



### ABSTRACT CLASSES ###



### POLYMORPHISM ###