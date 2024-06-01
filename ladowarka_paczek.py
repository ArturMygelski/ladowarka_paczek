print("witaj w naszej sortowni paczek")
ilosc_przedmiotow = int(input("podaj proszę ile przedmiotów chcesz wysłać - podaj wartość liczbową "))
waga_przedmiotów = 0
ilosc_paczek = 1
max_waga_paczki = 20
waga_obecnej_paczki = 0
max_wykorzystanie_wagi = 0
numer_paczki_z_max_wykorzystaniem_wagi = 1
for przedmiot in range(ilosc_przedmiotow):
    waga_przedmiotu = int(input(f"podaj wagę przedmiotu {przedmiot+1}: "))
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
        print("podano nieprawidłową wagę przedmiotu")
if max_waga_paczki - waga_obecnej_paczki > max_wykorzystanie_wagi:
    max_wykorzystanie_wagi = max_waga_paczki - waga_obecnej_paczki
    numer_paczki_z_max_wykorzystaniem_wagi = ilosc_paczek

if ilosc_paczek == 1:
    poprawny_wyraz = "paczkę"
elif 2 <= ilosc_paczek <= 4:
    poprawny_wyraz = "paczki"
else:
    poprawny_wyraz = "paczek"

print(f"wysłano {ilosc_paczek} {poprawny_wyraz} ")
print(f"wysłano {waga_przedmiotów} kg")
print(f"suma pustych kilogramów: {ilosc_paczek * max_waga_paczki - waga_przedmiotów} kg")
print(f"najwiecej pustych kilogramów ma paczka: {numer_paczki_z_max_wykorzystaniem_wagi} ({max_wykorzystanie_wagi} kg)")
