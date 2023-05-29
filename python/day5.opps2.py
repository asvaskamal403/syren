class dog:
    #class attribute
    attr1='barking'
    def __init__(self,name):
        self.name=name
t=dog('tommy')
j=dog('juno')
print('data with tommy:',t.attr1)
print('data with juno:',t.__class__.attr1)

#instance attribute
print('data with tommy:',t.name)
print('data with juno:',j.name)