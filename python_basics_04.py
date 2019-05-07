

def citanie_zo_suboru():

    # named parameters
    # f = open(mode="x", file="casopisy.txt")

    f = open("knihy.txt", "r")
    # cely_text = f.read()

    vsetky_riadky = f.readlines()
    print(vsetky_riadky)
    print("3.riadok: {} ".format(vsetky_riadky[2]))

    # print(jeden_riadok)

    # while jeden_riadok:
    #     novy_riadok = f.readlines()
    #     print(novy_riadok)

    # jeden_riadok
    # print(type(cely_text))

    # print(cely_text)


def zapisovanie_do_suboru():
    # TODO: pouzitie python kniznic
    # f = open("resources/knihy2.txt", "r")
    # vsetky_knihy = f.read()
    # f.close()

    with open("resources/knihy2.txt", "a") as f:
        f.write("Sila pozitivneho myslenia")

    # print(vsetky_knihy)


def main():
    zapisovanie_do_suboru()


if __name__ == '__main__':
    main()