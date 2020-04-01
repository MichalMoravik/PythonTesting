import unittest
from unittest_data_provider import data_provider
from purchase import Purchase


class test_purchase(unittest.TestCase):

    data = lambda: ((0,), (1,), (6,), (7,))

    @data_provider(data)
    def test_increment_phonelines_success(self, data):
        # Arrange
        purchase = Purchase()
        # Act and Assert
        # We test both the valid upper boundary and valid lower boundary
        # for x in [0, 1, 6, 7]:
        purchase.phones_lines = data
        initial_price = purchase.price
        purchase.increment_phonelines()
        print(data)
        self.assertEqual(purchase.phones_lines, data + 1)
        self.assertEqual(purchase.price, initial_price + purchase.phone_lines_price)

    data = lambda: ((9,), (8,), (2,), (1,))

    @data_provider(data)
    def test_decrement_phonelines_success(self, data):
        # Arrange
        purchase = Purchase()
        # Act and Assert
        # We test both the valid upper boundary and valid lower boundary
        # for x in [9, 8, 2, 1]:
        purchase.phones_lines = data
        initial_price = purchase.price
        purchase.decrement_phonelines()
        print(data)
        self.assertEqual(purchase.phones_lines, data - 1)
        self.assertEqual(purchase.price, initial_price - purchase.phone_lines_price)

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
            purchase.change_internet_connection(purchase.internet_connection)
        )

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
        self.assertEqual(
            purchase.phones, ["Motorola G99", "iPhone 99", "Samsung Galaxy 99"]
        )

    def test_get_price_after_selecting_phone(self):
        # Arrange
        phonesDict = {"Motorola G99": 800}
        purchase = Purchase()

        # Act
        purchase.get_price_after_selecting_phone(phonesDict, "Motorola G99")

        # Assert
        # The new price should be updated - the price of the phone should be added to the total price
        self.assertEqual(purchase.price, 800)

    def test_get_price_after_unselecting_phone(self):
        # Arrange
        purchase = Purchase()
        purchase.phones = {"Motorola G99": 800}
        purchase.price = 800

        # Act
        purchase.get_price_after_unselecting_phone("Motorola G99")

        # Assert
        # The new price should be updated - the total price should be decremented by the price of the phone
        self.assertEqual(purchase.price, 0)
