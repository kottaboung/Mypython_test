#LAP5 64200002กฎทบวง

from functools import reduce
ListA = {1,2,3,4,5}

def exponent_addnum(ListA):
    sum = 0

    for i in ListA:
        sum = (i*i)+sum
        #print(sum)
    return sum

print(exponent_addnum(ListA))

ListB = list(map(lambda x : x**2,ListA))
sum2 = 0
for j in ListB:
    sum2 = sum2+j
print(sum2)