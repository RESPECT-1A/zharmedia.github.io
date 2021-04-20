import json
import datetime
import requests
from bs4 import BeautifulSoup

page = requests.get("https://www.republika.co.id/")
obj = BeautifulSoup(page.text, "html.parser")

print("menampilkan objek html")
print("====================================")
print(obj)

print("\nmenampilkan title browser tanpa tag")
print("====================================")
print(obj.title.text)

print("\nmMenampilkan Semua teks h2")
print("====================================")
for headline in obj.find_all("h2"):
    print(headline.text)

print("\nmMenampilkan Semua teks h2")
print("====================================")
print(obj.find_all("div", class_="bungkus_txt_headline_center"))

print("\nMenampilkan Semua teks h2")
print("====================================")
for headline in obj.find_all("div", class_="bungkus_txt_headline_center"):
    print(headline.find("h2").text)

print("\nMenyimpan headline pada file text")
print("====================================")
f = open("D:\\02 ZHAR'S PROJECT\JTK POLBAN\SEMESTER 2\Proyek 1\Tugas 6\headline.text", "w")
for headline in obj.find_all("div", class_="teaser_conten1_center"):
    try:
        f.write(headline.find("h2").text)
    except:
        continue
    f.write("\n")

for headline in obj.find_all("div", class_="teaser_conten1_center"):
    try:
        f.write(headline.find("h1").text)
    except:
        continue
    f.write("\n")

for headline in obj.find_all("div", class_="teaser_conten1_center"):
    try:
        f.write(headline.find("div", class_="date").text)
    except:
        continue
    f.write("\n")

for headline in obj.find_all("div", class_="teaser_conten1_center"):
    try:
        f.write(datetime.datetime.now())
    except:
        continue
    f.write("\n")
f.close()

data = []
f = open("D:\\02 ZHAR'S PROJECT\JTK POLBAN\SEMESTER 2\Proyek 1\Tugas 6\headline.json", "w")
for headline in obj.find_all("div", class_="teaser_conten1_center"):
    try:
        data.append({"judul": headline.find("h2").text,
                     "kategori": headline.find("h1").text,
                     "waktupublish": headline.find("div", class_="date").text,
                     "waktuscrapping": datetime.datetime.now().strftime("%d %B %Y %H:%M:%S")})
    except:
        continue
jdumps = json.dumps(data)
f.writelines(jdumps)
f.close()
