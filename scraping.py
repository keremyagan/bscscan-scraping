#Kerem YAGAN
#https://github.com/keremyagan
import requests
from bs4 import BeautifulSoup
import time
url="https://bscscan.com/tokentxns"

dosya1=input("1.Dosyanın Konumunu Giriniz(Yeni Tokenlar):")
dosya2=input("2.Dosyanın Konumunu Giriniz(Liste):")
tur_sayisi=0
while True:
    try:
        content=requests.get(url).content
        soup=BeautifulSoup(content,"html.parser")
        liste=soup.findAll("tr")
        for i in liste:
            icerik=open(dosya1,"r").readlines()
            file=open(dosya2,"a")
            file.write(i.text.split()[-1])
            file.write("\n")
            file.close()
            if (i.text.split()[-1]+"\n") not in icerik:
                file=open(dosya1,"a")
                file.write(i.text.split()[-1])
                file.write("\n")
                file.close()
        tur_sayisi=tur_sayisi+1
        time.sleep(0.2)
        print(f"Tur Sayısı:{tur_sayisi}")
    except Exception as err:
        print(err)
        


    





