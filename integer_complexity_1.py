from math import sqrt
from datetime import datetime

A = int(input("Ener a value: "))

startTime = datetime.now()
minimum = A+1

for factor1 in range(1,int(sqrt(A))):
    factor2 = A/factor1
    if (factor2%1) == 0:
        if (factor2 + factor1) < minimum:
            minimum = int(factor2 + factor1)
            final_factor1 = int(factor1)
            final_factor2 = int(factor2)
print("Code time:", datetime.now() - startTime)
print (A, "=>", minimum)
