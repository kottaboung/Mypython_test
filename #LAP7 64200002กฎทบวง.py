#LAP7 64200002กฎทบวง

from functools import reduce
ListA = {1,2,3,4,5}

def addnumber(ListA):
    sum = 0
    for i in ListA:
        sum + i+sum
        #print(sum)
    return sum

print(addnumber(ListA))

sum2 = reduce((lambda x,y : x+y), ListA)
print(sum2)