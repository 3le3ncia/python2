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