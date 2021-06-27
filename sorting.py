#Kerem YAGAN
#https://github.com/keremyagan
from collections import Counter

dosya=input("Lütfen Dosya Konumunu Giriniz:")
ilk_kac_token=int(input("İlk Kaç Token Yazdırılsın:"))
icerik=open(dosya,"r").readlines()
siralama=Counter(icerik).most_common()
a=1
for i in siralama[:ilk_kac_token]:
    print(a,"-",i[0].rstrip("\n"),i[1])
    a=a+1
