slowa = ["burak", "cukinia", "pomidor", "cytryna", "ananas", "papryka", "dynia"]
litera = input("Podaj literę: ")
pasujaceslowa = [word for word in slowa if word.startswith(litera.lower())]
print(f"Słowa zaczynające się na literę {litera}: {pasujaceslowa}")