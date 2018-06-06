#!/usr/bin/env python3
# -*- coding: utf-8 -*-



def legendre_symbol(a, p):
    """ Compute the Legendre symbol a|p using
        Euler's criterion. p is a prime, a is
        relatively prime to p (if p divides
        a, then a|p = 0)

        Returns 1 if a has a square root modulo
        p, -1 otherwise.
    """
    ls = pow((int)(a), (int)((p - 1) / 2), (int)(p))
    return -1 if ls == p - 1 else ls


def QuadraticResidues(a,p):
   
    if a%p == 0:
        print("#########Symbole de Legendre############")
        print("(a|p) == 0")
        return
    a = a%p
    qr = []
    nqr = []

    for i in range(2,p):
        n = 0
        q = 1
        while(q!=1 or n==0):
            q = q*i %p
            n = n+1
        if n == p-1:
            qr.append(i)
        else:
            nqr.append(i)

    primitive = qr[0]
    primitive2 = (primitive**2)%p
    euler1 = (p-1)/2
    euler2 = (a**euler1)%p
    test = primitive2

    if euler2 == 1: #résidue quadratique test
        if(primitive2 == a):
            root == primitive
        else :
            r = 1
            while(test != a):
                r = r+1
                test = (primitive2**r)%p
            root = (primitive**r)%p
        print("#########Symbole de Legendre############")        
        print("(a|p) == 1")
        print(a," est un résidue quadratique")
        print("La racine carrée modulaire de cet entier: ",root)
        return root
    else:
        print("#########Symbole de Legendre############")
        print("(a|p) == -1")
        print(a," est un nonrésidue quadratique")
        return None


def Legendre(a,p):
   
    if a%p == 0:
        print("#########Symbole de Legendre############")
        print("(a|p) == 0")
        return 0
    a = a%p
    qr = []
    nqr = []
    
    for i in range(2,p):
        n = 0
        q = 1
        while(q!=1 or n==0):
            q = q*i %p
            n = n+1
        if n == p-1:
            qr.append(i)
        else:
            nqr.append(i)

    primitive = qr[0]
    primitive2 = (primitive**2)%p
    euler1 = (p-1)/2
    print("xixixixixhahah",a,euler1,p)
    euler2 = (a**euler1)%p
    test = primitive2

    if euler2 == 1: #résidue quadratique test
        return 1
        if(primitive2 == a):
            root == primitive
        else :
            r = 1
            while(test != a):
                r = r+1
                test = (primitive2**r)%p
            root = (primitive**r)%p
        print("#########Symbole de Legendre############")        
        print("(a|p) == 1")
        print(a," est un résidue quadratique")
        print("La racine carrée modulaire de cet entier: ",root)
        return 1
    else:
        print("#########Symbole de Legendre############")
        print("(a|p) == -1")
        print(a," est un nonrésidue quadratique")
        return -1

if __name__ == '__main__':

    print("Entrez a (nombre à vérifier)")
    a = int(input())
    print("Entrez p (nombre premier impair )")
    p = int(input())

    QuadraticResidues(a,p)
