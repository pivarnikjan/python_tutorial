MENA = ["Jan", "Peter", "Martinka", "Adela"]
VEK = [28, None, 30, 31]

VEK_LUDI = {
    "Jan": 28,
    "Peter": None
}
ZLOZITE_MENA = (("Jan", "Pivarnik"), ("Peter", "Blasko"))
tmp = [(meno, priezvisko) for meno, priezvisko in ZLOZITE_MENA]


ADRESY = {
    "Jan": "Chlebarova 9",
    "Peter": "Paprikova 7",
    "Maros": "Slaninova 12"
}


def for_cyklus_priklad():
    # 1. iterovanie cez list
    for meno in MENA:
        print(meno)

    # for pocitadlo in range(0, 6):
    # for pocitadlo in range(6): - koncovy prvok
    for pocitadlo in range(0, 6, 2):
        print(pocitadlo)

    for idx, value in enumerate(MENA):
        print("{0}, {1}".format(idx, value))

    # 2. iterovanie cez dict
    # mozno pouzit unpacking
    # for kluc, hodnotu in ADRESY.items():
    #     print(kluc, hodnotu)

    # for (meno, priezvisko) in ZLOZITE_MENA:
    #     print("{} {}".format(meno, priezvisko))


def while_cyklus_priklad():
    pocitadlo = 0

    # pokym je podmienka PRAVDA (TRUE)
    while pocitadlo < 5:
        print(pocitadlo)
        # pocitadlo = pocitadlo + 1
        pocitadlo += 1


def list_comprehension():

    # stary zapis
    # zoznam_statov = []
    # for meno in MENA:
    #     zoznam_statov.append((meno, "Slovensko"))

    zoznam_statov = [(meno, "SLovensko") for meno in MENA]

    print(zoznam_statov)

    # stary zapis
    # zaujimave_adresy = []
    # for meno in MENA:
    #     if meno in ADRESY:
    #         zaujimave_adresy.append("Meno: {}, Adresa: {}".format(meno, ADRESY[meno]))
    # print(zaujimave_adresy)

    zaujimave_adresy = [("Meno: {}, Adresa: {}".format(meno, ADRESY[meno])) for meno in MENA if meno in ADRESY]
    print(zaujimave_adresy)


def dict_comprehension():

    vek_ludi = {}
    for idx, meno in enumerate(MENA):
        vek_ludi[meno] = VEK[idx]
    print(vek_ludi)

    vek_ludi = {meno: VEK[idx] for idx, meno in enumerate(MENA)}
    print(vek_ludi)


def main():
    for_cyklus_priklad()
    while_cyklus_priklad()
    list_comprehension()
    dict_comprehension()


if __name__ == '__main__':
    # Tato funkcia povie pythonu, co ma spustit ak sa subor python_basics_03.py spusti ako skript

    # Spustenie suboru ako skript
    # python python_basics_03.py

    main()
