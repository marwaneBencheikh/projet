client={1:["hussame",28,100],2:["sihame",30,500],3:["faid",19,600]}
def ajouter_client():
    nom=input("taper votre nom:")
    age=int(input("taper votre age:"))
    solde=int(input("taper votre solde:"))
    cl=max(client.keys())+1
    client[cl]=[nom,age,solde]
print("ajouter un client:")  
ajouter_client()