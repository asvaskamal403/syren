# polymorphism || overriding

class Polygon:
    # method
    def render(self):
        print('Creating Polygon')

class Square(Polygon):
    def render(self):
        print('Creting Square')

class Circle(Polygon):
    def render(self):
        print('Creating Circle')
    
# creating object for square
s1 = Square()
s1.render()

#  creating object for class circle

c1 = Circle()
c1.render()