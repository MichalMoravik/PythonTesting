import unittest
from purchase import Purchase


class test_purchase(unittest.TestCase):
    def test_increment_phonelines_success(self):
        # Arrange
        purchase = Purchase()
        # Act and Assert
        # We test both the valid upper boundary and valid lower boundary
        for x in [0, 1, 6, 7]:
            purchase.phones_lines = x
            purchase.increment_phonelines()
            self.assertEqual(purchase.phones_lines, x + 1)

    def test_decrement_phonelines_success(self):
        # Arrange
        purchase = Purchase()
        # Act and Assert
        # We test both the valid upper boundary and valid lower boundary
        for x in [9, 8, 2, 1]:
            purchase.phones_lines = x
            purchase.decrement_phonelines()
            self.assertEqual(purchase.phones_lines, x - 1)

    def test_increment_phonelines_fail(self):
        # Arrange
        purchase = Purchase()
        # We test invaild upper boundary
        purchase = Purchase()
        purchase.phones_lines = purchase.max_phone_lines

        with self.assertRaises(ValueError):
            purchase.increment_phonelines()

    def test_decrement_phonelines_fail(self):
        # Arrange
        purchase = Purchase()
        # We test invaild lower boundary.
        purchase.phones_lines = 0
        with self.assertRaises(ValueError):
            purchase.decrement_phonelines()

    def test_internet_connection_True_and_check_price(self):
        # We call on the function purchase.change_internet_connection.
        # The function takes 1 boolean parameter.
        # We insert self.purchase.internet_connection which is supposed to be True.
        self.purchase.change_internet_connection(self.purchase.internet_connection)
        self.assertTrue(self.purchase.internet_connection)
        # If the self.purchase.internet_connection is True.
        # Then the self.purchase.price should be equal to 200.
        self.assertEqual(self.purchase.price, 200)

    def test_internet_connection_False_and_check_price(self):
        # We set self.purchase.internet_connection to be False.
        self.purchase.internet_connection = False
        # We check if purchase.change_internet_connection(self.purchase.internet_connection) is False.
        self.assertFalse(
            self.purchase.change_internet_connection(self.purchase.internet_connection)
        )
        # If it is False then purchase.price should be equal 0.
        self.assertEqual(self.purchase.price, 0)

    def test_buy_Fail(self):
        # We check if purchase.phones list is empty.
        self.assertEqual(self.purchase.phones, [])
        # If it is then an error message will appear.
        with self.assertRaises(ValueError):
            self.purchase.buy()

    def test_buy_Success(self):
        # We make a for loop to check several inputs.
        for x in ["Motorola G99", "iPhone 99", "Samsung Galaxy 99"]:
            self.purchase.phones.append(x)
            self.purchase.buy()
        # We check if purchase.phones list is equal to the inputs.
        self.assertEqual(
            self.purchase.phones, ["Motorola G99", "iPhone 99", "Samsung Galaxy 99"]
        )

    def test_selecting_phone(self):
        # Arrange
        phonesDict = {"Motorola G99": 800}
        purchase = Purchase()

        # Act
        self.purchase.selecting_phone(self.phones, phonesDict, "Motorola G99")

        # Assert
        self.assertEqual(len(self.purchase.phones), 1)

    def test_unselecting_phone(self):
        
