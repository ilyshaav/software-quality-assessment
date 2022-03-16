import requests
from bs4 import BeautifulSoup
import urllib
from urllib.request import urlretrieve
url = 'https://1000.menu/catalog/popular/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
# название, ссылка на фото, ссылка на контент
nameArray=[]
imageArray=[]
linkArray=[]

bufArray=[]
for link in soup.find_all('img'):
    nameArray.append(link.get('alt'))
    imageArray.append("http:" + str(link.get('data-original')))
nameArray.pop(0)
nameArray.pop(0)
imageArray.pop(0)
imageArray.pop(0) 

for i in nameArray:
    linkArray.append("https://1000.menu" +soup.find('a', title = str(i)).get('href'))

for i in range(len(nameArray)):
    bufArray.append(nameArray[i])
    bufArray.append(imageArray[i])
    bufArray.append(linkArray[i])

for i in bufArray:
    print(i)

links= open("links.txt","w")
for line in linkArray:
    links.write(line)
    links.write("\n")
links.close()

for i in range(len(nameArray)):
    r = requests.get(str(imageArray[i]))
    with open(str(i)+".jpg", "wb") as code:
        code.write(r.content)
    
