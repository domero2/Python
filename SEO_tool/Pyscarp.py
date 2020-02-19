import requests
import os
from bs4 import BeautifulSoup


class Pyscarp():
    def __init__(self):
        pass

    def creat_file_from_web(self, url):
        response = requests.get(url)
        print(response)
        soup = BeautifulSoup(response.text, features="lxml")
        all_a_atribute_on_side = soup.findAll('a')
        return all_a_atribute_on_side

    def save_all_into_file(self, file_name: str, url: str):
        if not file_name and not url:
            exit
        else:
            with open(os.path.join('/Users/amajcher/Desktop/BS', file_name), 'w+') as Fileproc:
                for item in self.creat_file_from_web(url):
                    Fileproc.write('%s\n' % item)

    def search_word_from_file(self,file_name, searching_word):

        with open(os.path.join('/Users/amajcher/Desktop/BS', file_name), 'r') as file:
            contents = file.read()
            search_word = searching_word
            FirstList = contents.split()
            Linkslist = []
            Imglist = []
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
            return SpliterListlink, SpliterListimage
