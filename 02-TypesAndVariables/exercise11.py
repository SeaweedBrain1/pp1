dochody_ojca = input("Enter father's income: ")
dochody_matki = input("Enter mother's income: ")
ilosc_czlonkow_rodziny = int(input("Enter number of people in family: "))
suma_dochodow = int(dochody_ojca) + int(dochody_matki)
print(f'Total income: {suma_dochodow}')
dochod_na_osobe = suma_dochodow / ilosc_czlonkow_rodziny
print(f'Income per peroson: {dochod_na_osobe}')

