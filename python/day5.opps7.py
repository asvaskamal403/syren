#multiple inheritance

#parent1
class parent1:
    def __init__(self,name):
        self.name=name
    def sit(self):
        print('i can sit')

#parent 2
class parent2:
    def __init__(self,name):
        self.name=name
    def stand(self):
        print('i can stand')


#child class
class child(parent1,parent2):
    def details(self):
        print("my name")

#object creation 
ganesh=child('ganesh')
ganesh.sit()
ganesh.stand()
ganesh.details()
