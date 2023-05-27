import random

while True:
    a = random.randint(0, 100)
    strzal = 0

    while True:
        num = int(input("Zgadnij liczbę: "))
        strzal += 1

        if num == a:
            print("Brawo! Odgadłeś liczbę po", strzal, "strzałach.")
            break
        elif num < a:
            print("Liczba jest większa.")
        else:
            print("Liczba jest mniejsza.")

    play_again = input("Czy chcesz zagrać jeszcze raz? (Tak/Nie): ")
    if play_again.lower() != "tak":
        break
