import requests
import os
from bs4 import BeautifulSoup

#Funcion responsible for create list of a elements in web
def creat_file_from_web(url):
    response = requests.get(url)
    print(response)
    soup = BeautifulSoup(response.text,features="lxml")
    all_a_atribute_on_side=soup.findAll('a')
    return all_a_atribute_on_side

#Function responsible for sav into desktop directory file with txt format
def save_all_into_file(file_name: str, url: str):
    with open(os.path.join('/Users/amajcher/Desktop',file_name),'w+') as Fileproc:
        for item in creat_file_from_web(url):
            Fileproc.write('%s\n' % item)
            
#Function responsible for searching choseen word from file, and print list of images and list of lnks
def search_word_from_file(file_name,searching_word):
    with open(os.path.join('/Users/amajcher/Desktop', file_name),'r') as file:
        contents = file.read()
        search_word = searching_word
        FirstList = contents.split()
        Linkslist = []
        Imglist= []
        for i in FirstList:
            if search_word.lower() in i:
                if 'uploads' in i:
                    Imglist.append(i)
                elif 'href' in i:
                    Linkslist.append(i)
                else:
                    pass
        SpliterListlink = set(Linkslist)
        SpliterListimage = set(Imglist)
        print("All links contains %s" % search_word)
        print('\n'.join(SpliterListlink))
        print("All images contains %s" % search_word)
        print('\n'.join(SpliterListimage))

save_all_into_file('links2.txt','http://amadeuszmajcher.pl/blog/')

search_word_from_file('links2.txt','trener')



