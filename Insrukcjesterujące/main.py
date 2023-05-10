#zadanie1
wiek = int(input("Ile masz lat: "))
if wiek >= 18:
    print("Jesteś pełnoletni")
else:
    print("Jesteś niepełnoletni")

#zadanie2
for i in range(0, 100):
    if i%3 == 0:
        print(i)
#zadanie3
import random
a = random.randint(0, 100)
while(True):
    num = int(input())
    if num == a:
        print("super")
    elif num < a:
        print('Liczba jest większa')
    else:
        print('liczba jest mniejsza')