import math


def delitele (n):
    for i in range(1, n):
    
        if n % i == 0:
            print(i)


n = int(input("zadej lib. cislo:"))