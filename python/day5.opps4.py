#single level inheritance
#parent class
class wild_animal:
    def __init__(self,name):
        self.name=name
    def speak(self):
        print('i am a',self.name)

#child class
class dog(wild_animal):
    def bark(self):
        print('woof!')

#object creation
mydog=dog('harsha')
mydog.speak()
mydog.bark()