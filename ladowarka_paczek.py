print("witaj w naszej sortowni paczek")
ilosc_przedmiotow = int(input("podaj proszę ile przedmiotów chcesz wysłać - podaj wartość liczbową "))
waga_przedmiotów = 0
ilosc_paczek = 1
max_waga_paczki = 20
waga_obecnej_paczki = 0
max_wykorzystanie_wagi = 0
numer_paczki_z_max_wykorzystaniem_wagi = 1
for przedmiot in range(ilosc_przedmiotow):
    waga_przedmiotu = int(input("podaj ilosc wagę każdego z przedmiotów: "))
    if 1 <= waga_przedmiotu <= 10:
        waga_przedmiotów += waga_przedmiotu
        if waga_przedmiotu + waga_obecnej_paczki > max_waga_paczki:
            if max_waga_paczki - waga_obecnej_paczki > max_wykorzystanie_wagi:
                max_wykorzystanie_wagi = max_waga_paczki - waga_obecnej_paczki
                numer_paczki_z_max_wykorzystaniem_wagi = ilosc_paczek
            ilosc_paczek += 1
            waga_obecnej_paczki = waga_przedmiotu
        else:
            waga_obecnej_paczki += waga_przedmiotu
    else:
        print("przedmiot nie mieści się w zakresie referencyjnym 1-20")
if max_waga_paczki - waga_obecnej_paczki > max_wykorzystanie_wagi:
    max_wykorzystanie_wagi = max_waga_paczki - waga_obecnej_paczki
    numer_paczki_z_max_wykorzystaniem_wagi = ilosc_paczek

print(f"ilosc dodanych przedmiotów ogółem to: {ilosc_przedmiotow}")
print(f"waga wszystkich przedmiotów to {waga_przedmiotów}")
print(f"suma paczek to: {ilosc_paczek}")
print(f"suma pustych kilogramów w paczkach to: {ilosc_paczek * max_waga_paczki - waga_przedmiotów}")
print(f"najwiecej pustych kilogramów: {max_wykorzystanie_wagi}, w paczce nr paczki: {numer_paczki_z_max_wykorzystaniem_wagi}")
