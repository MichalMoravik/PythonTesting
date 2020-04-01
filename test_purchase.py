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
         # Arrange
        purchase = Purchase()
        purchase.internet_connection = True

        # Act
        # We call on the function purchase.change_internet_connection.
        # The function takes 1 boolean parameter.
        # We insert purchase.internet_connection which is supposed to be True.
        purchase.change_internet_connection(purchase.internet_connection)

        # Assert
        self.assertTrue(purchase.internet_connection)
        # If the purchase.internet_connection is True.
        # Then the purchase.price should be equal to 200.
        self.assertEqual(purchase.price, 200)

    def test_internet_connection_False_and_check_price(self):
         # Arrange
        purchase = Purchase()
        # We set self.purchase.internet_connection to be False.
        purchase.internet_connection = False

        # Act
        purchase.change_internet_connection(purchase.internet_connection)

        # Assert
        # We check if purchase.change_internet_connection(self.purchase.internet_connection) is False.
        self.assertFalse(
            purchase.change_internet_connection(purchase.internet_connection))

        # If it is False then purchase.price should be equal 0.
        self.assertEqual(purchase.price, 0)

    def test_buy_Fail(self):
        # Arrange
        purchase = Purchase()

        # Act
        # If it is then an error message will appear.
        with self.assertRaises(ValueError):
            purchase.buy()

        # Assert
        # We check if purchase.phones list is empty.
        self.assertEqual(purchase.phones, [])
        

    def test_buy_Success(self):
        # Arrange
        purchase = Purchase()
        # We make a for loop to check several inputs.
        for x in ["Motorola G99", "iPhone 99", "Samsung Galaxy 99"]:
            purchase.phones.append(x)

            # Act
            purchase.buy()

            # Assert
        # We check if purchase.phones list is equal to the inputs.
        self.assertEqual(purchase.phones, ["Motorola G99", "iPhone 99", "Samsung Galaxy 99"])

    def test_selecting_phone(self):
        # Arrange
        phonesDict = {"Motorola G99": 800}
        purchase = Purchase()

        # Act
        self.purchase.selecting_phone(self.phones, phonesDict, "Motorola G99")

        # Assert
        self.assertEqual(len(self.purchase.phones), 1)

    # def test_unselecting_phone(self):