nom=input("taper votre nom:")
age=input("taper votre age:")
note=input("taper votre note:")
file=open("ficher.txt","a")
file.write(nom+"\n"+age+"\n"+note+'\n')
file.close()


file=open("ficher.txt","r")
print(file.read())
file.close()