class User:
    def __init__(self, first_name, last_name):
        self.name = first_name
        self.surname = last_name

    def print_name(self):
        print("Моё имя:", self.name)

    def print_surname(self):
        print("Моя фамилия:", self.surname)

    def print_my_name_is(self):
        print("Меня зовут:", self.name, self.surname)

        