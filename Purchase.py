class Purchase:
    def __init__(self):
        self.internet_connection = True
        self.phones_lines = 0
        self.cell_phones = []
        self.price = 0


        def internet_connection(self, user_choices):
            if user_choices:
                self.price += 200
            else:
                self.price -=200

            return self.price


        
        def buy(self):
            if self.price == 0:
                try:
                    print()
                
                except ValueError:
                    print("Please add something to the list")
