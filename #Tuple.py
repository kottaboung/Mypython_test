#Tuple

tp1 =(111, 222, 333)
tp2 =(520 , 1200)
tp3 =('Python', 'C#', 'OCP')

def PrintData(*data):
    print(*data)

PrintData(tp1)
PrintData(tp2)
PrintData(tp3)