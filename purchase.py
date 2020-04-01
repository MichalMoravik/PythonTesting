# example of possible phones dictionary
# phonesDict = {
#     "Motorola G99": 800,
#     "iPhone 99": 6000,
#     "Samsung Galaxy 99": 1000,
#     "Sony Xperia 99": 900,
#     "Huawei 99": 900,
# }


class Purchase:
    def __init__(self):
        self.internet_connection = False
        self.phones_lines = 0
        self.phones = []
        self.price = 0

    # We use the change_internet_connection method to charge the user for the internet connection.
    def change_internet_connection(self, internet_connection):
        # If the internet_connection is true we charge the user 200.
        if self.internet_connection == True:
            self.price += 200

        return self.price

    # We use the buy method to check if the user bought something or not.
    def buy(self):
        if self.phones == []:
            raise ValueError("Please add something to the list")
        else:
            print("Proceed to the next page")

    def increment_phonelines(self):
        if self.phones_lines < 8:
            self.phones_lines += 1
        else:
            self.phones_lines = 8
            raise ValueError(
                "Invalid input. The maximum number of phone lines that can be hired is 8"
            )

    def decrement_phonelines(self):
        if self.phones_lines > 0:
            self.phones_lines -= 1
        else:
            raise ValueError(
                "Invalid input. The number of phone lines cannot be negative"
            )

    def selecting_phone(self, phones, phone_name):
        if phone_name in phones:
            self.phones.append(phone_name)
            self.price = self.price + phones[phone_name]
            return self.price
        else:
            print("The phone does not exist!")

    def unselecting_phone(self, phones, phone_name):
        if phone_name in self.phones:
            self.phones.remove(phone_name)
            self.price = self.price - phones[phone_name]
            return self.price
        else:
            print("The phone does not exist!")
