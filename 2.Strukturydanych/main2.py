slowo = input("Podaj słowo: ")
if slowo == slowo[::-1]:
    print(f"Słowo {slowo} jest palindromem.")
else:
    print(f"Słowo {slowo} nie jest palindromem.")