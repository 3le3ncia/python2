wiek = int(input("wiek: "))
a2 = input("A2 od co najmniej 2 lat? (tak/nie): ")
if wiek >= 24 or (a2 == "tak" and wiek >= 20):
    print("Tak")
else:
    print("Nie")