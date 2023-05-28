count=0
count1=0
list1=[]
list2=[]
f2=open("harsha.txt","r")
for i in f2:
    for j in i.split(" "):
        for k in j:
            if(k in ['a','e','i','o','u','A','E','I','O','U']):
                count=count+1
                if k not in list1:

                    list1.append(k)
            else:
                count1=count1+1
                if k not in list2:
                    list2.append(k)
sum1=count+count1
print("vowel %=" ,(count/sum1)*100)
print("consonants %=" ,(count1/sum1)*100)
print(list1)
print(list2)