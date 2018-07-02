#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
from time import time
from fractions import gcd
import PrdNobPrm
import Legendre
import numpy as np
from scipy.linalg import solve
from itertools import chain

def FactorBase(longeur=5):
    T = []
    for i in PrdNobPrm.primes():
        if longeur>0:
            if i==2:
                T.append(i)
                longeur = longeur - 1
            elif Legendre.legendre_symbol(n,i) == 1:
                T.append(i)
                longeur = longeur - 1
        else: 
            return T

def ChoisieDesQ(n,taille = 100):
    
    Q = lambda x: (x+int(math.sqrt(n)))**2-n
    T = []
    for i in range(1,taille):
        T.append(Q(i))
    return T

def QuadraticSieve(T,S):
    
    M1 = [[0]*len(S) for i in range(len(T))]
    for i in range(len(S)):
        for j in range(len(T)):
            cp = 0
            while T[j]%S[i] == 0:
                cp = cp+1
                T[j] = T[j]/S[i]    
            M1[j][i] = cp%2
    M2 = []
    M3 = []
    for a in range(len(T)):
        if T[a] == 1:
            M2.append(M1[a])
            M3.append(a+1)
    return M2,M3

def FastGauss(M,S):
    # reference: A Fast Algorithm for Gaussian Elimination Over GF(2) and its Implementation on the GAPP
    # Çetin K.KOÇ AND SARATH N.ARACHCHIGE
    
    for i in range(len(M)):
        if M[i] == [0]*len(M[0]):
            return [i]

    # print("M : ",M)
    N = transpose(M)
    marks = [False]*len(N[0])
    lg = len(N)

    for j in range(lg): # horizontale
        for i in range(len(N[j])): # verticale
            if N[j][i] == 1:
                marks[i] = True
                for k in range(lg):
                    if k != j:
                        if N[k][i] == 1:
                            AddMatCol(N,j,k)
    
    R = []
    result = []
    print("N : ", N)
    print("marks : ",marks)
    
    for v in range(len(N[0])):  #verticale
        if marks[v] == False:
            # il y a solution
            for h in range(len(N)):
                if N[h][v] == 1:
                    for t in (len(N[0])):
                        if t != v and N[h][t] == 1:
                            print("Great")
                            R.append(t)
                            break
            R.append(v)
    
    # il n'y a pas de solution

    if R == []:
        print("On n'a pas de solution")
        return None
    else:
        print("Solution :", R)
        return R

def RefaireEtape3(ent,S):
    global cpt
    cpt = cpt+1
    T = ChoisieDesQ(ent)
    M,X = QuadraticSieve(T,S)
    Re,Xi = FastGauss(ent,M,S,X)
    return Re,Xi

def SolutionRows(N,R,marks):
    res = [] 
    for i in R: # cols
        print("cols : ", i)
        for j in range(len(N[i])): # rows
            print("rows : ",j)
            if N[i][j] == 1 and marks[j]== True:
                res.append(j)
                print("mmmmmmmmmmmmmmmmmxxxxxxxxxxxxeijfeiffjk",res)
    if res == []:
        print("Pas de solutions, il faut ajouter des variable dans le 3ème étape")
        return None
    
    res.append(h) 
    return res


def FastGaussCOR(M,S):
    # reference: A Fast Algorithm for Gaussian Elimination Over GF(2) and its Implementation on the GAPP
    # Çetin K.KOÇ AND SARATH N.ARACHCHIGE
    
    m = len(M)
    R = [False]*m
    for i in range(len(M)):
        if M[i] == [0]*len(M[0]):
            R[i] = True
            return R
    
    n = len(M[0])
    marks = [False]*m
    nStar = n
    for i in range(n):
        for j in range(m):
            if M[j][i] == 1 and nStar > 0:
                marks[j] = True
                nStar = nStar - 1
                for k in range(n):
                    if k != i:
                        if M[j][k] == 1:
                            AddMatCol(M,i,k)
                            print(M)
    
    print("marks : ",marks)
    print("M : ",M)
    for v in range(m):
        if marks[v] == False:
            # il y a des solutions
            for h in range(n):
                if M[v][h] == 1:
                    for t in range(m):
                        if marks[t] == True and M[t][h] == 1:
                            R[t] = True
            R[v] = True
        break

    if R == [False]*m:
        print("On n'a pas de solution, il faut prendre plus de Xi")
        return 
    else:
        print("Solution : ", R)
        return R



def AddMatCol11(N,i,k):
    for j in range(len(N[j])):
        N[k][i] = (N[k][i] + N[j][i])%2

def AddMatCol(M,i,k):
    for a in range(len(M)):
        M[a][k] = (M[a][k] + M[a][i])%2

def gauss_elim(M):
    #mprint(M)
    #M = optimize(M)
    marks = [False]*len(M[0])
    
    for i in range(len(M)): #do for all rows
        row = M[i]
        #print(row)
        
        for num in row: #search for pivot
            if num == 1:
                #print("found pivot at column " + str(row.index(num)+1))
                j = row.index(num) # column index
                marks[j] = True
                
                for k in chain(range(0,i),range(i+1,len(M))): #search for other 1s in the same column
                    if M[k][j] == 1:
                        for i in range(len(M[k])):
                            M[k][i] = (M[k][i] + row[i])%2
                break
            
    print(marks)
    M = transpose(M)
    #mprint(M)
    
    sol_rows = []
    for i in range(len(marks)): #find free columns (which have now become rows)
        if marks[i]== False:
            free_row = [M[i],i]
            sol_rows.append(free_row)
    
    if not sol_rows:
        return("No solution found. Need more smooth numbers.")

    print("Found {} potential solutions".format(len(sol_rows)))
    return sol_rows,marks,M


def transpose(matrix):
    #transpose matrix so columns become rows, makes list comp easier to work with
    new_matrix = []
    for i in range(len(matrix[0])):
        new_row = []
        for row in matrix:
            new_row.append(row[i])
        new_matrix.append(new_row)
    return(new_matrix)

def resultat(R,Xi):
    rf = [] 
    for i in range(len(R)):
        if R[i] == True:
            rf.append(Xi[i])

    Q = lambda x: (x+int(math.sqrt(n)))**2-n
    
    print("Résultat final : ",rf)
    g = 1
    for j in rf:
       g=g*Q(j) 
    
    d = 1
    for j in rf:
        d=d*(j+int(math.sqrt(n)))

    g = (int)(math.sqrt(g))   

    print("p :", gcd(g+d,n))
    print("q :", gcd(abs(g-d),n))

    return


if __name__ == '__main__':

    print("###########################")
    print("# Algo Crible Quadratique #")
    print("###########################")
    
    # (1) Obtient un nombre entier
    print("Entrez un nombre entier: ")
    n = int(input())

    # (2) Factor base
    time_dep = time()
    S = FactorBase(10)
    print("S :",S)
   
    # (3) Choisie des Q(x)
    T = ChoisieDesQ(n,10000)

    # (4) Tamis Quadratique (Quadratic sieve)
    M,X = QuadraticSieve(T,S) # M est la matrice de 
    print("M : ",M)
    print("Xi : ",X)

    
    # (5) Résoudre les matrices
    Re = FastGaussCOR(M,S)
    
    # (6) Résultat
    resultat(Re,X)    
    
    t = time() - time_dep
    print("Temps :", t)   


