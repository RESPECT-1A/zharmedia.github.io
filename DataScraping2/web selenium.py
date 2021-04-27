from selenium import webdriver
import urllib.request
from selenium.common.exceptions import NoSuchElementException
import json
from datetime import datetime

PATH = "D:\Kuliah\Semester 2\Project 1\Web Selenium\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.billboard.com/charts/artist-100")

artistlist = []
i = 1

now = datetime.now()
time = now.strftime("%d %B %Y %H:%M:%S")

for artist in driver.find_elements_by_class_name("chart-list-item"):
    print(artist.text)
    print(artist.find_element_by_class_name("chart-list-item__image").get_attribute("src"))
    # urllib.request.urlretrieve(artist.find_element_by_class_name("chart-list-item__image").get_attribute("src"), str(i)+".png")
    artistlist.append(
                {
                    "Rank": artist.text.split('\n')[0],
                    "Name": artist.text.split('\n')[1],
                    "Last": artist.text.split('\n')[2].split(' ')[0],
                    "Peak": artist.text.split('\n')[2].split(' ')[3],
                    "Weeks": artist.text.split('\n')[2].split(' ')[6],
                    "TimeToScrapping": time,
                    "Profile": artist.find_element_by_class_name("chart-list-item__image").get_attribute("src")
                }
            )

hasil_scrapping = open("hasilscraping.json", "w")
json.dump(artistlist, hasil_scrapping, indent=6)
hasil_scrapping.close()
driver.quit()