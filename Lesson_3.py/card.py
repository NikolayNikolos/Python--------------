class Card:
    number = "0000 0000 0000 0000"
    valiDate = "01/99"
    holder = "unknown"

    def __init__(self, number, date, holder):
        self.holder = holder
        self.number = number
        self.date = date

    def pay(self, amount):
        print("С карты" , self.number, "списали", amount)



  