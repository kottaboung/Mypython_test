#LAP4 64200002กฎทบวง

from functools import reduce

ListA = {1,2,3,4,5}
sum = []

def exponent(a):
    for i in a:
        sum.append(i**2)
    return sum

print(exponent(ListA))

print(list(map(lambda x : x**2,ListA)))