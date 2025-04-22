from addres import Address

class Mailing:
    to_address : Address
    from_address : Address
    track = "TRK000"
    cost = "0000"
    def __init__(self, to_address, from_address, cost, track):
        self.to_address = to_address
        self.from_address = from_address
        self.cost = cost
        self.track = track

   
    #def sum(self,cost):
       # print(f"Отправление {self.track} из {self.to_address} в {self.from_address} Стоимость {cost} рублей.")