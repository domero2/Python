def inna_funkcja():
    print("inna funkcja")

def dekorator(obj):
    return inna_funkcja

@dekorator
def funkcja():
    print("hello")

funkcja()


class Zwierze:
    def __init__(self, nazwa, wiek, waga):
        self.nazwa = nazwa
        self.wiek = wiek
        self.waga = waga

    def przedstaw_sie(self):
        print(f"Jestem zwierzęciem {self.nazwa}, mam {self.wiek} lat oraz wazę {self.waga} kg.")

    def urodziny(self):
        self.wiek += 1


class Slon(Zwierze):
    def przedstaw_sie(self):
        print(f"Jestem sloniem {self.nazwa}, mam {self.wiek} lat oraz wazę {self.waga} kg.")


class Lew(Zwierze):
    pass


class Papuga(Zwierze):
    pass

class Lew(Zwierze):
    def przedstaw_sie(self):
        super().przedstaw_sie()
        print("A tak w ogóle to jestem lwem")



Dumboo = Slon("Dumboo", 77, 6000)
Simba = Lew("Simba", 24, 100)
Jago = Papuga("Jago", 32, 3)
jakis_zwierz = Zwierze("cos", 31, 80)

Dumboo.przedstaw_sie()
Simba.przedstaw_sie()
jakis_zwierz.przedstaw_sie()

Jago.urodziny()
Jago.przedstaw_sie()

print('\n\n-----')

def decor_func(some_f):
    def inside_func(*args, **kwargs):
        print("started")
        ret = some_f(*args, **kwargs)
        print("Ended")
        return ret

    return inside_func

def some_func():
    print('New inside func')

def new_func():
    print('New func1')

x =decor_func(some_func)
x()
print('\n\n-----')


@decor_func
def new_func2():
    print('New func2')



@decor_func
def args_func(x, y):
    print(f'it is my arg: {x}')
    return y
new_func2()

print('\n-----')

args_func(89,12)