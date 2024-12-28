import csv
file= open("file.csv","a")
var=csv.reader(file,delimiter=";")
def ajouter_elev():
    nom=input("taper votre nom:")
    age=input("taper votre age:")
    math=input("taper la note de math:")
    pysique=input("taper la note de physique:")
    english=input("taper la note de english:")
    file.write(nom+";"+age+";"+math+";"+pysique+";"+english)
 
ajouter_elev()
def moyenne(matiere):
    s=0
    for k in var:
        if k==matiere:
            s+=[k]
    m=s/4
    print(m)
