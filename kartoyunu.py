import random

simgeler = ["Karo","Maça","Sinek","Kupa"]
sayilar = [1,2,3,4,5,6,7,8,9,10,"Joker","Kız","Papaz"]
kagitlar=[]

for simge in simgeler:
    for sayi in sayilar:
        kagitlar.append(simge + " " + str(sayi) )

oyuncular={}

for oyuncu in range(1,5):
    oyuncular["Oyuncu " + str(oyuncu)] = []
    for kart in range(1,5):
        kagit = kagitlar.pop(kagitlar.index(random.choice(kagitlar)))
        oyuncular["Oyuncu "+ str(oyuncu)].append(kagit)

for i in sorted(oyuncular):
    print (i + "\n" + "--------")
    for k in oyuncular[i]:
        print (k)
