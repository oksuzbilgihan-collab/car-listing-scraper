import os
os.system("cls")   # Windows
from bs4 import BeautifulSoup
import requests
import pandas as pd
liste = []
with open("sample_truecar.html","r",encoding="utf-8") as dosya:
    html = dosya.read()

headers = {"user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36"} 

soup = BeautifulSoup(html, "lxml")

k1 = soup.find_all("div",class_="flex w-full flex-col h-full items-center")
for i1 in k1 :
    a1 = i1.find("h2")
    if a1 :
        a11 = a1.text.strip()
    else :
        a11 ="none"
    # marka
    a2 = i1.find("div",class_="text-14 font-bold line-clamp-1")
    if a2 :
        a22 = a2.text.strip()
    else :
        a22 = "none"

    # model
    a3 = i1.find("div",class_="text-24 font-bold")
    if a3 :
        a33 = a3.text.strip()
    else :
        a33 = "none"
    # fiyat
    a4 = i1.find("a",attrs={"data-test":"listingCarouselImageLink"})
    a5 = a4.get("href")
    # linkler
    a6 = "https://www.truecar.com"+ a5
    

    liste.append([a11,a22,a33,a6])

df = pd.DataFrame(liste)
df.columns=["Marka","Model","Fiyat","Link"]
print(df)
df.to_excel("car.listing.xlsx",index=False)



