#!/usr/bin/env python3

import random
from time import time

def pgcd(a,b):
    while b>0:
        a,b=b,a%b
    return a

def PollardRho(n):

    f = lambda x: x*x + random.randint(2,10)
    x, y, d= 2, 2, 1
    while d==1:
        x = f(x)%n
        y = f(f(y))%n
        d = pgcd(abs(x-y),n)
    return d


if __name__ == '__main__':
    print("Entrez un nombre entier")
    n = int(input())
    dep = time()
    d = PollardRho(n)
    temp = time()-dep

    if d==1 or d==n:
        print("Le nombre est premier")
    else:
        print("Le nombre n'est pas premier")
    print(n, "=", d, "*", (int)(n/d))
    print("Temps: ", temp)
