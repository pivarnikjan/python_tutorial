# PRIRADENIE
# pocitadlo = 0
# --------------------------------------------------------
# POROVNANIE
# if pocitadlo == 1:
#     print('Pocitadlo sa rovna 1')
# else:
#     print("Pocitadlo sa nerovna 1")
# --------------------------------------------------------
# CYKLUS
# <0, 5)
# for i in range(0, 5):
#     print(i)

# --------------------------------------------------------


# BEZ POUZITIA FUNKCII

# slovnaft jozko
# plat = 500
# premie = 50
# vysledna_vyplata = plat + premie
# print(vysledna_vyplata)

# slovnaft anicka
# plat = 400
# premie = 50
# vysledna_vyplata = plat + premie
# print(vysledna_vyplata)

# slovnaft ferka
# plat = 400
# premie = 50
# vysledna_vyplata = plat + premie
# print(vysledna_vyplata)

# ibm jozko
# plat = 400
# premie = 50
# vysledna_vyplata = plat + premie
# print(vysledna_vyplata)

# ibm anicka
# plat = 400
# premie = 50
# vysledna_vyplata = plat + premie
# print(vysledna_vyplata)

# ibm ferka
# plat = 400
# premie = 50
# vysledna_vyplata = plat + premie
# print(vysledna_vyplata)

# --------------------------------------------------------


# PROCEDURALNE PROGRAMOVANIE
def vysledna_vyplata(plat, premie):
    return plat + premie


def vyplaty_pre_slovnaft_team():
    ferkov_plat = vysledna_vyplata(500, 60)
    anickin_plat = vysledna_vyplata(400, 60)
    jozkov_plat = vysledna_vyplata(1000, 60)

    print("Ferkov plat: ", ferkov_plat, "\n Anickin plat: ", anickin_plat, "\n Jozkov plat:", jozkov_plat)


def vyplaty_pre_ibm_team():
    ferkov_plat = vysledna_vyplata(500, 80)
    anickin_plat = vysledna_vyplata(400, 80)
    jozkov_plat = vysledna_vyplata(1000, 80)

    print("Ferkov plat: ", ferkov_plat, "\n Anickin plat: ", anickin_plat, "\n Jozkov plat:", jozkov_plat)


def vyplaty_vo_firmach_proceduralne():
    print("PROCEDURALNE PROGRAMOVANIE")
    vyplaty_pre_slovnaft_team()
    vyplaty_pre_ibm_team()

# --------------------------------------------------------


# OBJEKTOVO ORIENTOVANE PROGRAMOVANIE
class FIRMA:

    def __init__(self, premia):
        self.premia = premia

    def vypis_vyplaty_pre_team(self):
        ferkov_plat = vysledna_vyplata(500, self.premia)
        anickin_plat = vysledna_vyplata(400, self.premia)
        jozkov_plat = vysledna_vyplata(1000, self.premia)

        print("Ferkov plat: ", ferkov_plat, "\n Anickin plat: ", anickin_plat, "\n Jozkov plat:", jozkov_plat)


def vyplaty_vo_firmach_objektovo():
    print("OBJEKTOVO ORIENTOVANE PROGRAMOVANIE")
    slovnaft = FIRMA(premia=60)
    slovnaft.vypis_vyplaty_pre_team()

    ibm = FIRMA(premia=80)
    ibm.vypis_vyplaty_pre_team()

# --------------------------------------------------------


def main():
    vyplaty_vo_firmach_proceduralne()
    vyplaty_vo_firmach_objektovo()


if __name__ == '__main__':
    # Tato funkcia povie pythonu, co ma spustit ak sa subor python_basics_01.py spusti ako skript

    # Spustenie suboru ako skript
    # python python_basics_01.py

    main()

