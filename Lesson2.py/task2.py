is_year_leap = input("Введите год:")
year = int(is_year_leap)
if (year % 4 == 0):     
        print(f"Год {is_year_leap}: True")  
else:
        print(f"Год {is_year_leap}: False")