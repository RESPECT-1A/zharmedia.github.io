from selenium import webdriver
import urllib.request
from selenium.common.exceptions import NoSuchElementException
import json
import datetime

PATH = "D:\\02 ZHAR'S PROJECT\\JTK POLBAN\\SEMESTER 2\\Proyek 1\\Tugas 7\\chromedriver_win32\\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get(
    "https://screenagewasteland.com/the-100-greatest-cartoons-of-all-time-10-1/")

animelist = []
i = 1

while i <= 100:
    for artist in driver.find_elements_by_class_name("entry-content"):
        driver.execute_script(
            "arguments[0].scrollIntoView();", artist)  # auto scroll
        print(artist.text)
        for img in artist.find_elements_by_class_name("aligncenter"):
            try:
                url = img.get_attribute("src")
                urllib.request.urlretrieve(url, str(i)+".png")
                print(url)
            except:
                continue
            i = i+1
            animelist.append(
                {
                    "Keterangan": artist.text.split("\n")[3],
                    "Judul": artist.text.split("\n")[1],
                    "Rating": artist.text.split("\n")[5].split()[0],
                    "Image": img.get_attribute("src"),
                    "waktuscrapping": datetime.datetime.now().strftime("%d %B %Y %H:%M:%S")
                }
            )
    try:
        driver.find_element_by_class_name(
            "pagination").find_element_by_partial_link_text("Next").click()
    except NoSuchElementException as e:
        break

hasil_scrapping = open("hasilscraping.json", "w")
json.dump(animelist, hasil_scrapping, indent=6)
hasil_scrapping.close()
driver.quit()
