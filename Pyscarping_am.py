import requests
from bs4 import BeautifulSoup


#We are checking all a 
url = 'http://amadeuszmajcher.pl/blog/'
response = requests.get(url)
print(response)
soup = BeautifulSoup(response.text,features="lxml")
kok=soup.findAll('a')

#Create file links.txt and add all a tags from website

with open('links.txt','w+') as Fileproc:
    for item in kok:
        Fileproc.write('%s\n' % item)