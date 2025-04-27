class Address:
    #index = "000000"
    #city = "String"
    #street = "string"
    #home = "0"
    #apartment = "0"

    def __init__(self, index, city, street, home, apartment):
        self.index = index
        self.city = city
        self.street = street
        self.home = home
        self.apartment = apartment
    def adres(self):
        print(self.index, self.city,  self.street, self.home, self.apartment)   