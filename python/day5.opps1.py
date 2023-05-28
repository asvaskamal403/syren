class dog:
    def __init__(self,name,breed,age):
        self.name=name
        self.breed=breed
        self.age=age
    def bark(self):
        print('woof!')
    def wag_tail(self):
        print('my tail is wagging')
    def display(self):
        print('my name is :',self.name)
        print('my age is :',self.age)
#creating object

mydog=dog('harsha','daborman','90')
mydog.bark()
mydog.wag_tail()
mydog.display()