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


def main():
    Dumboo = Slon("Dumboo", 77, 6000)
    Simba = Lew("Simba", 24, 100)
    Jago = Papuga("Jago", 32, 3)
    jakis_zwierz = Zwierze("cos", 31, 80)

    Dumboo.przedstaw_sie()
    Simba.przedstaw_sie()
    jakis_zwierz.przedstaw_sie()

    Jago.urodziny()
    Jago.przedstaw_sie()


if __name__ == "__main__":
    main()
