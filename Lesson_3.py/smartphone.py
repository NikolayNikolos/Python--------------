class smartphone:

    def __init__(self,phone_brand,phone_model,nomer):
        self.phone_brand = phone_brand
        self.phone_model = phone_model
        self.nomer = nomer
    def Brend(self):
        print("Моя марка телефона", self.phone_brand) 

    def Model(self):
        print("Моя модель телефона", self.phone_model)

    def Nomer(self):
        print("Мой номер" , self.nomer)   

my_smartphone = smartphone("ihpone", "pro16", "+7(999)555-55-55")                
my_smartphone.Brend()
my_smartphone.Model()
my_smartphone.Nomer()
