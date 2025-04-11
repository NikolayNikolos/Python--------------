def bank(x,y):
    for i in range(y):
      x += (x * 0.1)
    return(f"Сумма на счете спустя {y} ktn {x:.2f} рублей ")

x = int(input("Введите сумму"))
y = int(input("Введите срок на который хотите сделать вклад"))
print(bank(x,y))