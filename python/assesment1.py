#!/usr/bin/env python
# coding: utf-8

# In[19]:


#1
for i in range(1,11):
    for j in range(1,6):
        print(i*j,end="\t")
    print()    


# In[20]:


#2
num=int(input("enter the number:"))
sum=0
while(num>0):
    a=num%10
    sum = sum + a
    num=num//10
print("sum is",sum)    


# In[50]:


#3
num=int(input())
l=len(str(num))
sum=0
while(num>0):
    a=num%10
    sum=sum + (a*(10**(l-1)))
    l=l-1
    num=num//10
print("reverse is",sum)


# In[21]:


#4
num=int(input("enter the number:"))
b=num
l=len(str(num))
sum=0
while(num>0):
    a=num%10
    sum=sum + (a**l)
    num=num//10
print("sum is",sum)
if(sum==b):
    print("so it is a amstrong number")
else:
    print("not an amstrong number")


# In[22]:


#5
count=0
for i in range(2001,2301):
    if(i%3==0):
        count=count+1
        print(i,end=" , ")
        if(count==5):
            break
        


# In[23]:


#6
for i in range(301,401):
    if(i%7==0):
        continue
    else:
        print(i,end=" ")


# In[43]:


#7
num=int(input("enter the number:"))
fact=1
for i in range(1,num+1):
    fact=fact*i
print(num,"! = ",end="")    
for i in range(num,0,-1):
    print(i,end=".")

print(" = ",fact)    


# In[44]:


#8
name= str(input())
count=0
for i in name:
    if (i=='A' or i=='E' or i=='I' or i=='O' or i=='U' or i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
        count=count+1
print("count of vowels are:",count)


# In[74]:


#9
name= str(input().strip(""))
l=len(name)
vcount=0
ccount=0
for i in name:
    if (i=='A' or i=='E' or i=='I' or i=='O' or i=='U' or i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
        vcount=vcount+1
    if(i>'A' and i<'Z') or (i>'a' and i<'z'):
        if(i!='A' or i!='E' or i!='I' or i!='O' or i!='U' or i!='a' or i!='e' or i!='i' or i!='o' or i!='u'):
            ccount=ccount +1
print("count of vowels are:",vcount)
print("count of consonants are:",ccount)


# In[ ]:


#10
a=int(input("enter the value of a:"))
b=int(input("enter the value of b:"))
c=int(input("enter the value of c:"))
if(a>b and a>c):
    print("a is max")
elif(b>a and b>c):
    print("b is max")
else:
    print("c is max")


# In[73]:


n=int(input())
sum=0
l=len(str(n))
for i in range(l):
    a=n%10
    sum=sum + a*(10**(l-1))
    l=l-1
    n=n//10
print(sum)    
    


# In[6]:


msg="asvas kamal"
for i in range(len(msg)):
    print("msg[" +str(i)+"] = ",msg[i])


# In[24]:


#positive index
kamal=(1,2,3,4,5,6,7)
print(kamal[::2])
print(kamal[1:5:2])
print(kamal[1::-2])
print(kamal[::-2])
print(kamal[2:2:2])


# In[25]:


#negative index
print(kamal[-1:-7:-1])
print(kamal[-2:-3:-2])
print(kamal[-1:-7:-2])
print(kamal[-2:-4:-1])
print(kamal[-7:-2:1])


# In[26]:


tup1=(1,2,3,4,5,6,7,8,9,0)
kamal=tuple(i for i in tup1)
print(kamal)


# In[16]:


harsha=[]
for i in range(len(kamal)):
    if i%2==0:
        harsha.append(kamal[i])
print(harsha)        


# In[23]:


k=["@gmail@yahoo.com","vikas@gmail.com","kamal@gmail.com","harsha.a@syrencloud.com","saiakamal.a@syrencloud.com"]
a=[]
b=[]
c=''
for i in k:
    if "gmail.com" in i:
        a.append(i)
print(a)
for i in a:
    for j in i:
        if j=="@":
            break
        else:
            c=c+j
    b.append(c)
    c=""
print(b)    


# In[32]:


x=int(input())
def factorial(x):
    fact=1
    for i in range(1,x+1):
        fact=fact*i
    return fact  
print(factorial(x))


# In[ ]:





# In[ ]:


5

