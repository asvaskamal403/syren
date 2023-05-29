import statistics as s
def cal_area(width,height):
    return width*height
width=5
def cal_average(l):
    return s.mean(l)
def reverse_string(s):
    a=s[::-1]
    return a
def ispalindrome(s):
    a=s[::-1]
    print(a)
    if (a==s):
        return True
    else:
        return False
def power_of_two(n):
    if(n>0):
        while(n%2==0):
            n=n//2
        if(n==1):
            return True
        else:
            return False      
print(cal_area(5,10))
print(cal_average([2,4,6,8,10]))
print(reverse_string("Hello, World!"))  
print(ispalindrome("radar"))
print(power_of_two(16))        
