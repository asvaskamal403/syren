#heirarchy inheritance
#parent class
class animal:
    def __init__(self,name):
        self.name=name
    def bark(self):
        print('hehe you are dog',self.name)

#child class 1
class ganesh(animal):
    def breed(self):
        print('i am chihuaha breed of dogs')

#child class 2
class sai(animal):
    def fetch(self):
        print("shocked!! i can print from here also")

#object creation
dog1=ganesh('ganesh')
dog1.bark()
dog1.breed()

dog2=sai('sai')
dog2.bark()
dog2.fetch()
