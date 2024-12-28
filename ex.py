t=[10,20,30,40,50,60,70,80,90 , None]

n=[None]*10

nb=int(input("taper un nombre"))

for i in range(0,9):
    if t[i]<nb:
        n[i]=t[i]
    else:
        break
print(n)
n[i]=nb
for j in range(i+1,10):
        n[j]=t[j-1]
print(n)
            

        



