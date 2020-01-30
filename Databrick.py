import os
import math
from inheritance import Astronomer
from colorama import Fore
import openpyxl
class Databricks(Astronomer):

    def __init__(self):
        #Astronomer.__init__(self,task_id='456id')
        print('databricks created')

firsdatabricks = Databricks()
seconddatabrick = firsdatabricks.astro_run()

class SublimeText():
    def __init__(self, name: str):
        self.name = name
    def return_input(self):
        raise NotImplementedError("lolz")

class Book():
    def __init__(self,title: str, author: str, pages: int ):
        self.title = title
        self.author = author
        self.pages = pages
    def __str__(self):
        return f" author: {self.author} title:  {self.title} pages: {self.pages}"

    def __len__(self):
        return self.pages

b = Book(title='Somebook',author='Jarek', pages=23)

print(b)
print(len(b))

class Line():
    def __init__(self, cor1: tuple, cor2: tuple):
        self.cor1 = cor1
        self.cor2 = cor2

    def distance(self):
        firstarg= (self.cor2[0] - self.cor1[0])
        secondarg=(self.cor2[1] - self.cor1[1])
        d = math.pow(firstarg,2) + math.pow(secondarg,2)
        g = math.sqrt(d)
        return g
    def slope(self):
        firstarg=(self.cor2[1]-self.cor2[0])
        secondarg = (self.cor1[1] - self.cor1[0])
        d = firstarg/secondarg
        return d

cordinate1=(3,2)
cordiante2 = (8,10)
koko = Line(cordinate1,cordiante2)
print(koko.distance())
print(koko.slope())

class Account():
    def __init__(self, owner: str, ballance: float):
        self.owner = owner
        self. ballance = ballance

    def deposit(self,amount):
        self.ballance += amount
        print('Deposit Accepted')
        return self.ballance

    def withdraw(self, withdraw):
        if withdraw > self.ballance:
            print('nor enough founds')

        else: print('Withdraw accepted')
        self.ballance -= withdraw
        return self.ballance

    def check_ballance(self):
        print(f"you have yet: {self.ballance} ammount of money")

    def __str__(self):
        return f"Owner: {self.ballance}\n Ballance: {self.ballance}"

wallet = Account(owner='Jaro', ballance=100)

wallet.deposit(10)

wallet.withdraw(20)

wallet.check_ballance()

print(Fore.RED + "some text")