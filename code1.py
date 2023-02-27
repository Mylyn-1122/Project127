from bs4 import BeautifulSoup
import requests
import csv
START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
x=requests.get(START_URL)
soup=BeautifulSoup(x.content, "html.parser")
headers=["Name","Distance","Mass","Radius"]
starData=[]
    


table1=soup.find("table",attrs={"class","wikitable sortable"})
templist=[]
for tr_tags in table1.find_all("tr"):
    td_tag=tr_tags.find_all("td")
    row=[i.text.rstrip() for i in td_tag]
    templist.append(row)
    
templist.pop(0)


for i in range(0,len(templist)):

    templist2=templist[i]

    templist2.pop(4),templist2.pop(3),templist2.pop(2),templist2.pop(0)

    
    starData.append(templist2)

    


with open("scraper.csv","w") as f:
    csvwriter=csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(starData)



