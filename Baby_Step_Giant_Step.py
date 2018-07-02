# Baby Step Giant Step DLP problem y = a**x mod n 
# Example 70 = 2**x mod 131
# Use SAGE for complex operations
import math 

print("Sous form de y = a**x mod n :  ")
print("Entrez y")
y = int(input())

print("Entrez a")
a = int(input())

print("Entrez n")
n = int(input())
 
s = math.floor(math.sqrt(n))
 
A = []
B = []
 
for r in range(0,s):
    value = y*(a^r) % n
    A.append(value)
 
for t in range(1,s+1):
    value = a^(t*s) % n
    B.append(value)
 
print(A)
print(B)
 
x1,x2 =0,0
  
for r in A:
    for t in B:
        if r == t:
            x1 = A.index(r)            
            x2 = B.index(t)
            print(x1)
            print(x2)
            break
             
 
print('the value of x is ', ((x2+1)*s - x1) % n) # Answer
