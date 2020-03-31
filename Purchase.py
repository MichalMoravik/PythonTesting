class Purchase:
    def __init__(self):
        self.id = id
        self.internet_connection = True
        self.phones_lines = 0
        self.phones = []
        self.price = 0

    def internet_connection(self):
        if internet_connection == True:
            self.price += 200
        else:
            self.price -= 200

    def buy(self):
        if self.price == 0:
            try:
                print()

            except ValueError:
                print("Please add something to the list")

    def increment_phonelines(self):
        self.phones_lines += 1
        if self.phones_lines > 8:
            self.phones_lines = 8
            raise ValueError(
                "The maximum number of phone lines that can be hired is 8!"
            )

    def decrement_phonelines(self):
        self.phones_lines -= 1
        if self.phones_lines < 0:
            raise ValueError("The number of phone lines cannot be negative!")

    def selecting_phone(self, phone_name):
        self.phones.append(phone_name)

    def unselecting_phone(self, phone_name):
        self.phones.remove(phone_name)
