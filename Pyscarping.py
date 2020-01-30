import requests
import os
from bs4 import BeautifulSoup


m=0
url = 'http://amadeuszmajcher.pl/blog/'
response = requests.get(url)
print(response)
soup = BeautifulSoup(response.text,features="lxml")
kok=soup.findAll('a')

#with open(os.path.join('/Users/amajcher/Desktop','links.txt'),'w+') as Fileproc:
 #   for item in kok:
  #      Fileproc.write('%s\n' % item)


#with open(os.path.join('/Users/amajcher/Desktop','links.txt'),'r') as file:
 #   contents = file.read()
  #  search_word = 'trener'
   # if search_word in contents:
    #    print ('word found',contents)
   # else:
     #   print ('word not found')


with open(os.path.join('/Users/amajcher/Desktop','links.txt'),'r') as file:
    contents = file.read()
    search_word = 'trener'
    FirstList = contents.split()
    FinalList = []
    for i in FirstList:
        if search_word.lower() in i:
            FinalList.append(i)
    SpliterList = set(FinalList)
    print('\n'.join(SpliterList))


