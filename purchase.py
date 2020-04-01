class Purchase:
    def __init__(self):
        self.internet_connection = False
        self.phones_lines = 0
        self.phones = {}
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

    # Add new key-value pair from available dictionary of phones to Purchase's dictionary of phones
    # Update Purchase's price
    # Return price
    def get_price_after_selecting_phone(self, phonesDictionary, phone_name):
        if phone_name in phonesDictionary:
            self.price = self.price + phonesDictionary[phone_name]
            self.phones[phone_name] = phonesDictionary[phone_name]
            return self.price
        else:
            raise ValueError("The phone does not exist!")

    # Delete key-value pair from Purchase's dictionary of phones
    # Update Purchase's price
    # Return price
    def get_price_after_unselecting_phone(self, phone_name):
        if phone_name in self.phones:
            self.price = self.price - self.phones[phone_name]
            del self.phones[phone_name]
            return self.price
        else:
            raise ValueError("The phone does not exist!")
