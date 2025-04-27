class User:
    def __init__(self, first_name, last_name):
        self.name = first_name
        self.surname = last_name

    def my_Name(self):
        print("Моё имя:", self.name)

    def sur_Name(self):
        print("Моя фамилия:", self.surname)

    def My_name_is(self):
        print("Меня зовут:", self.name, self.surname)

        