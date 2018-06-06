#!/usr/bin/env python3

import random
from time import time
import math
from fractions import gcd
def pgcd(a,b):
    while b>0:
        a,b=b,a%b
    return a

def PollardRho(n):

    f = lambda x: x*x + 2
    x, y, d= 2, 2, 1
    cp = 0
    while d==1:
        cp = cp + 1
        x = f(x)%n
        y = f(f(y))%n
        d = gcd(abs(x-y),n)

    return d,cp

def PollardRho2(n):

    f = lambda x: x*x + 2
    x, y, d= 2, 2, 1
    cp = 0
    m = 10
    tmp = 1
    while d==1:
        cp = cp + 1
        x = f(x)%n
        y = f(f(y))%n
        tmp = (tmp*abs(x-y))%n
        if cp%m == 0:
            d = gcd(tmp,n)
    return d,cp

def algoNif(n):
    cp = 0
    for i in range(3,(int)(math.sqrt(n)),2):
        cp = cp+1
        if n%i == 0:
            return i,cp
    return ""

if __name__ == '__main__':
    
    
    print("Entrez un nombre entier")
    n = int(input())
    
    ###__PollardRho__###
    dep = time()
    d,cp = PollardRho(n)
    temp = time()-dep
    
    print("Méthode PollardRho")
    if d==1 or d==n:
        print("Le nombre est premier")
    else:
        print("Le nombre n'est pas premier")
    
    print(n, "=", d, "*", (int)(n/d))
    print(cp, "tour")
    '''print(d)'''
    print("Temps: ", temp)
    print("######################################")

    ###__PollardRhoAmeliore__###
    dep = time()
    d,cp = PollardRho2(n)
    temp = time()-dep
   
    print("Méthode PollardRho amélioré")
    if d==1 or d==n:
        print("Le nombre est premier")
    else:
        print("Le nombre n'est pas premier")
    
    print(n, "=", d, "*", (int)(n/d))
    print(cp, "tour")
    '''print(d)'''
    print("Temps: ", temp)   
    print("######################################")

    ###__MethodNaif__###
    dep = time()
    d, cp =algoNif(n)
    temp = time() - dep
    print(n, "=", d, "*", (int)(n/d))
    print(cp, "tour")
    '''print(d)'''
    print("Temps: ", temp)


