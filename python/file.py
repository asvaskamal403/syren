linec=0
wordc=0
spacec=0
charc=0
f1=open("harsha.txt","r")
for i in f1:
    linec=linec+1
    for j in i.split():
        wordc=wordc+1
        for k in j:
            charc=charc+1
print(linec)
print(wordc)
spacec=wordc-1
print(spacec)
print(charc) 
f1.close()               

    