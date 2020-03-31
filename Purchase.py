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
        if self.price == 0:
            raise ValueError("Please add something to the list")
        else:
            print("Proceed to the next page")

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
