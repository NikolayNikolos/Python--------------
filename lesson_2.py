# Задание 0
my_age = input("my_age: ") 
my_age = int(my_age)
print (f"Ваш возраст: {my_age}" )

my_age =  my_age + 1
print (f"Ваш обновленный возраст: {my_age}" )

# задание1

lst = ["Виноград",
       "Персик",
       "Груша",
       "Апельсин",
       "Банан",
       "Яблоко"]
fruits = lst[0]
print(fruits)
fruits = lst[5]
print(fruits)

# Задание 2 Високосный годь Создайте функцию is_year_leap, 
#  принимающую 1 аргумент — год (число) — и возвращающую True,
#  если год високосный, и False — иначе.
is_year_leap = input("Введите год:")
year = int(is_year_leap)
if (year % 4 == 0):     
        print(f"Год {is_year_leap}: True")  
else:
        print(f"Год {is_year_leap}: False")

 # задание 3 Площадь квадрата
 
import math

def square(seid):
    result = seid * seid
    if not isinstance(seid, int):
        result = math.ceil(result)
    return 'Площадь квадрата' ,result
   
seid = float(input("Введите сторону квадрата: "))
print(square(seid))

# Задание 4
def fizz_buzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return 'FizzBuzz' 
    elif n % 5 == 0:
        return 'Buzz'
    elif n % 3 == 0:
        return 'Fizz'
    else:
        return (n)

    
n = int(input('Введите число:'))
print(fizz_buzz(n))

#Задание 5
def month_to_season(month):
    if month in  [12,1,2]:
        return "Зима"
    elif month in [3,4,5]:
        return "Весна"
    elif month in [6,7,8]:
        return "Лето"
    elif month in [9,10,11]:
        return "Осень"
    else:
        return "Неккоректный месяц"     


month = int(input("Введите месяц числом:"))  
print(month_to_season(month))

#Задание 6
lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]
for n in lst:
    if(n % 3 == 0) and (n < 30):
     print(n)
   

#Задание 7
lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]
list = sum(lst)
print(list)


#Задание 8
for i in range(18, 1, -4):
    print(i)

#Задание 9
var_1 = 37
var_2 = 99
var_1 = var_1 + var_2
var_2 = var_1 - var_2
var_1 = var_1 - var_2
print(var_1)
print(var_2)

#Задание 10

def bank(x,y):
    for i in range(y):
      x += (x * 0.1)
    return(f"Сумма на счете спустя {y} ktn {x:.2f} рублей ")

x = int(input("Введите сумму"))
y = int(input("Введите срок на который хотите сделать вклад"))
print(bank(x,y))