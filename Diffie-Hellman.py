# use Python 3 print function
# this allows this code to run on python 2.x and 3.x
from __future__ import print_function

print( "Nombre Premier publique: ")
sharedPrime = int(input())    # p
print( "Base publique:  ")
sharedBase = int(input())      # g
 
# Alice Sends Bob A = g^a mod p
print("Entrez Alice Secret")
aliceSecret = int(input())  # a
A = (sharedBase**aliceSecret) % sharedPrime
print( "Alice Sends Over Public Chanel: " , A )
 
# Bob Sends Alice B = g^b mod p
print("Entrez Bob Secret")
bobSecret = int(input())  # b
B = (sharedBase ** bobSecret) % sharedPrime
print( "Bob Sends Over Public Chanel: ", B )
 
print( "\n------------\n" )
print( "Privately Calculated Shared Secret:" )
# Alice Computes Shared Secret: s = B^a mod p
aliceSharedSecret = (B ** aliceSecret) % sharedPrime
print( "Alice Shared Secret: ", aliceSharedSecret )
 
# Bob Computes Shared Secret: s = A^b mod p
bobSharedSecret = (A**bobSecret) % sharedPrime
print( "Bob Shared Secret: ", bobSharedSecret )
