import numpy as np

L=list(range(10))

str_L=[str(c) for c in L]
#print(str_L) #prints the value 0 to 9

L2=np.zeros(10, dtype=int)
#print(L2) #print the array of zeroes

L3=np.ones((3,5,6), dtype=int)
#print(L3) #prints the array of defined size of ones

#print(np.full((5,6,7),1.23))

#print(np.arange(0,20,2))

#print(np.linspace(0,20,10))

#print(np.random.normal(0,2,(3,3)))

print(np.eye(4))