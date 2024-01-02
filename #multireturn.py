#multireturn

def Calculator(num1, num2):
    a = num1+num2
    ni = num1-num2
    nj = num1*num2

    if(num2 == 0):
        d = 0
    else:
        d = num1/num2

    return (a, ni, nj, d)

anwser = Calculator(210, 5  )
print(type(anwser))
print(anwser)
