class parrot:
    #class attribute
    name=''
    age=0
#object 1
p1=parrot()
p1.name='ganesh'
p1.age=90

#object 2
p2=parrot()
p2.name='sai'
p2.age=91

#access class attributes for different objects
print(p1.name,'is',p1.age,'years old')
print(p2.name,'is',p2.age,'years old')