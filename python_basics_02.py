

def list_priklad():
    """
    LIST

    - mozno modifikovat - menit mu jednotlive hodnoty (mutable)
    - ma zoradene prvky
    - hodnoty v liste sa mozu opakovat
    """
    print("LIST: ")

    moj_list = ['Jany', 10, 'jablko', 3.5, 'jablko']
    print(moj_list)

    print("Prvy prvok v poli je: {}".format(moj_list[0]))      # 0 je prvy prvok

    moj_list[1] = 20
    print(moj_list)

    moj_list.append('clovek')
    print(moj_list)


def tuple_priklad():
    """
    TUPLE

    - je imutable
        moj_list[1] = 20 vyfailuje

    - zoradene prvky
    - prvky sa mozu opakovat

    """
    print("TUPLE: ")

    # 1 - 4 -> Jany, 5 -> 10, 6 - 11 -> jablko, 12 -> 3.5, 6 - 11 -> jablko
    moj_tuple = ('Jany', 10, 'jablko', 3.5, 'jablko')
    print(moj_tuple)

    print("Prvy prvok tuple: " + moj_tuple[0])      # 0 je prvy prvok

    # je 3.prvok identicky s 5.prvkom?
    # odpoved: ANO je
    print(moj_tuple[2] is moj_tuple[4])


def set_priklad():
    """
    SET

    - si neuklada poradie, nema zoradene prvky
    - prvky su unikatne - nemozu sa opakovat
    - je imutable
        moj_set[0] = "Duri" vyfailuje
    """
    print("SET: ")

    moj_set = {"Jano", 1}
    print(moj_set)

    dlhy_list = [1, 1, 1, 2, 3, 5, 7, 8, 2, 1, 1, 3, 3, 5, 7, 1]
    unikatne_prvky = set(dlhy_list)
    print(unikatne_prvky)

    print(len(unikatne_prvky))


def dict_priklad():
    """
    DICT

    - prvky nie su zoradene
    - prvky mozno modifikovat su MUTABLE
    - kluc je unikatny, hodnota priradena klucu sa moze opakovat
    """

    print("DICT: ")

    moj_dict = {"C1": "Jano", "Martinka": 26, "C2": "Jano"}
    print(moj_dict)

    # takyto zapis sa moze na prvy pohlad javit ze pristupuje k 2.prvku v poli, no v skutocnosti vytvara novy objekt,
    # kde klucom je 1
    moj_dict[1] = "D1"
    print(moj_dict)

    moj_dict["Martinka"] = 27
    print(moj_dict)


def datove_typy():
    boolean_vyraz = True
    print("BOOLEAN: ", type(boolean_vyraz))

    cislo_cele = 5
    print("INT: ", type(cislo_cele))

    cislo_desatinne = 5.2
    print("FLOAT: ", type(cislo_desatinne))

    retazec = "Hello World"
    print("STRING: ", type(retazec))

    list_priklad()
    tuple_priklad()
    set_priklad()
    dict_priklad()


def priklad_na_formatovanie(meno, priezvisko, vek):

    # 1. spajanie stringov, kde neje osetreny typ
    # cele_meno_s_vekom = meno + priezvisko + vek

    # 2. spajanie stringov s osetrenym typom
    cele_meno_s_vekom = str(meno) + " " + str(priezvisko) + " " + str(vek)

    # 3. viac pythonovsky zapis za pouzitie format methody
    format_zapis = "{} {} {} {}".format(meno, priezvisko, vek, meno)

    # 3.1 zapis kde je prepouzita premenna 'meno'
    format_zapis_2 = "{0} {1} {2} {0}".format(meno, priezvisko, vek)

    # od PYTHON 3.6 - f-string najelegantnejsi zapis retazca
    # f_string = f'{meno} {priezvisko} {vek} {meno}'

    print(format_zapis_2)


def main():
    datove_typy()
    priklad_na_formatovanie("Jan", "Pivarnik", 28)


if __name__ == '__main__':
    # Tato funkcia povie pythonu, co ma spustit ak sa subor python_basics_02.py spusti ako skript

    # Spustenie suboru ako skript
    # python python_basics_02.py

    main()
