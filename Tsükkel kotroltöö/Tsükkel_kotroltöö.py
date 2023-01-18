#5 variant
import random

#1
#n=int(input("Kirjutage täisarv vahemikus 1 kuni 9: "))
#a1= " ~~~~~     "
#a2="/_____\    "
#a3="| []  |    "
#a4= " -----     "
#x=0
#while x<n:
#    if n>0 and n<10:
#        print(a1*n,a2*n,a3*n,a4*n,sep="\n")
#        break
#    else:
#        print("Sul oli vaja kijuta täisarv vahemikus 1 kuni 9!")

#2
õpilased=int(input("Inimeste arv esimesel klassis: "))
õpilased2=õpilased
klass=0
klass2=0
for x in range(õpilased):
    hind=random.randint(1,5)
    klass+=hind
for y in range(õpilased2):
        hind2=random.randint(1,5)
        klass2+=hind2
keskminehind=round(klass/õpilased,1)
keskminehind2=round(klass2/õpilased,1)
print("Esimesel klassis keskmine hind: ",keskminehind)
print("Teisel klassis keskmine hind: ",keskminehind2)


#4
#people=random.randint()