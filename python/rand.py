import math
x = int(input('Enter the value of x : '))
y = input('Enter the value of y : ')
try :
  print=(math.sqrt(x))
  print(x/y)
except ZeroDivisionError :
  print('Error : Please check the number')
except TypeError :
  print('Error : Please check the input')
except ValueError :
  print('Error : please see the number')  
except SyntaxError:
  print("syntax error")  