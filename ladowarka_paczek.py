print("witaj w naszej sortowni dokumentow")
ilosc_dokumentow = int(input("podaj prosze ile dokumentow chcesz posegregowac - podaj wartosc liczbowa "))
suma_stron = 0
ilosc_szafek = 1
pojemnosc_szafki = 100
pojemnosc_obecnej_szafki = 0
maksymalne_wolne_miejsce = 0
numer_szafki_z_max_pustym_miejscem = 1
ilosc_dodanych_dokumentow = 0
for dokument in range(ilosc_dokumentow):
    ilosc_stron = int(input("podaj ilosc stron dokumentu: "))
    if 1<= ilosc_stron <= 30:
        suma_stron += ilosc_stron
# pojemnosc_obecnej_szafki += ilosc_stron
        if ilosc_stron + pojemnosc_obecnej_szafki > pojemnosc_szafki:
            if pojemnosc_szafki - pojemnosc_obecnej_szafki > maksymalne_wolne_miejsce:
                maksymalne_wolne_miejsce = pojemnosc_szafki - pojemnosc_obecnej_szafki
                numer_szafki_z_max_pustym_miejscem = ilosc_szafek
            ilosc_szafek += 1
            pojemnosc_obecnej_szafki = ilosc_stron
        else:
            pojemnosc_obecnej_szafki += ilosc_stron
    else:
        print("ilosc stron nie miesci sie w zakresie referencyjnym 1-30")
if pojemnosc_szafki - pojemnosc_obecnej_szafki > maksymalne_wolne_miejsce:
    maksymalne_wolne_miejsce = pojemnosc_szafki - pojemnosc_obecnej_szafki
    numer_szafki_z_max_pustym_miejscem = ilosc_szafek

print(f"ilosc dodanych dokumentow to: {ilosc_dodanych_dokumentow}")
print(f"ilosc dodanych dokumentow to {ilosc_dokumentow} ")
print(f"suma stron dokumentow to {suma_stron}")
print(f"suma szafek to: {ilosc_szafek}")
print(f"suma wolnych miejsc w szafkach to: {ilosc_szafek * pojemnosc_szafki - suma_stron}")
print(f"najwiecej wolnego miejsca w szafce: {maksymalne_wolne_miejsce}, nr szafki: {numer_szafki_z_max_pustym_miejscem}")
