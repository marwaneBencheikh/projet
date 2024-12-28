def lis():
    s = 0
    l = [None]*10
    for i in range(0,10):
        l[i]=int(input("taper un nombre:"))
        s+=l[i]
    m= s / len(l)
    print("la moyeene est:",m)
    
