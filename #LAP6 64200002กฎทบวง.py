#LAP6 64200002กฎทบวง

from functools import reduce
ListA = {1,2,3,4,5}

def exponent_addnum(ListA):
    sum = 0
    for i in ListA:
        sum = i+sum
        #print(sum)
    return sum

print(exponent_addnum(ListA))

sum2 = reduce((lambda x,y : x+y), ListA)
print(sum2)