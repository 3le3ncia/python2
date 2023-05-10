#zadanie1
liczba = (10, -3, 4, 9, 12, -6, 0)
max_num = liczba[0]
min_num = liczba[0]
for num in liczba:
    if num > max_num:
        max_num = num
    if num < min_num:
        min_num = num
print(f"Największa liczba to: {max_num}")
print(f"Najmniejsza liczba to: {min_num}")
#zadanie2
slowo = input("Podaj słowo: ")
if slowo == slowo[::-1]:
    print(f"Słowo {slowo} jest palindromem.")
else:
    print(f"Słowo {slowo} nie jest palindromem.")
#zadanie 3
slowa = ["burak", "cukinia", "pomidor", "cytryna", "ananas", "papryka", "dynia"]
litera = input("Podaj literę: ")
pasujaceslowa = [word for word in slowa if word.startswith(litera.lower())]
print(f"Słowa zaczynające się na literę {litera}: {pasujaceslowa}")