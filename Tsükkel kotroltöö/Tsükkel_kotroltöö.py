#5 variant
import random

#Ülusanne 1
n=int(input("Sisestage majade arv 1 kuni 9: "))
maja="""
     ~~~~~     
    /_____\\    
    | []  |    
     -----     
"""
if n>0 and n<10:
    for i in range(n):
        if n>0 and n<9:
            print(maja, end=" ")
else:
    print("Sisestage arv vahemikus 1 kuni 9")


#Ülesanne 2
#print("Klassides on 10 õpilased")
#õpilased=10
#hinnad=[3, 4, 5, 2, 4, 5, 5, 4, 3, 5]
#hinnad2=[4, 5, 4, 3, 4, 2, 1, 3, 5, 5]
#klass=0
#klass2=0
#for i in range(õpilased):
#    klass+=hinnad[i]
#    klass2+=hinnad2[i]
#keskmine_hind=klass/õpilased
#keskmine_hind2=klass2/õpilased
#print("Esimesel klassis keskmine hind: ",keskmine_hind)
#print("Teisel klassis keskmine hind: ",keskmine_hind2)

#Ülusanne 3
#õpilased=random.randint(15, 30)
#min_hinne=5
#max_hinne=0
#for i in range(õpilased):
#    hinne=random.randint(1,5)
#    if hinne<min_hinne:
#        min_hinne=hinne
#    if hinne>max_hinne:
#        max_hinne=hinne

#print(f"Klassis on {õpilased} õpilased")
#print(f"Minimaalne hinne {min_hinne}")
#print(f"Maksimaalne hinne {max_hinne}")