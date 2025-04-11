import math

def square(seid):
    result = seid * seid
    if not isinstance(seid, int):
        result = math.ceil(result)
    return 'Площадь квадрата' ,result
   
seid = float(input("Введите сторону квадрата: "))
print(square(seid))