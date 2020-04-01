import unittest
from unittest_data_provider import data_provider
from purchase import Purchase


class test_purchase(unittest.TestCase):

    def valid_phone_lines(): return ((0,), (1,), (6,), (7,))

    @data_provider(valid_phone_lines)
    def test_increment_phonelines_success(self, valid_phone_lines):
        # Arrange
        purchase = Purchase()
        # Act and Assert
        # We test both the valid upper boundary and valid lower boundary
        # for x in [0, 1, 6, 7]:
        purchase.phones_lines = valid_phone_lines
        initial_price = purchase.price
        purchase.increment_phonelines()
        print(valid_phone_lines)
        self.assertEqual(purchase.phones_lines, valid_phone_lines + 1)
        self.assertEqual(purchase.price, initial_price +
                         purchase.phone_lines_price)

    def invalid_phone_lines(): return ((9,), (8,), (2,), (1,))

    @data_provider(invalid_phone_lines)
    def test_decrement_phonelines_success(self, invalid_phone_lines):
        # Arrange
        purchase = Purchase()
        # Act and Assert
        # We test both the valid upper boundary and valid lower boundary
        purchase.phones_lines = invalid_phone_lines
        initial_price = purchase.price
        purchase.decrement_phonelines()
        self.assertEqual(purchase.phones_lines, invalid_phone_lines - 1)
        self.assertEqual(purchase.price, initial_price -
                         purchase.phone_lines_price)

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
        self.assertEqual(purchase.phones, {})

    def valid_phone_list(): return (({"Motorola G99": 800},), ({
        "iPhone 99": 6000},), ({"Samsung Galaxy 99": 1000},))

    @data_provider(valid_phone_list)
    def test_buy_Success(self, valid_phone_list):
        # Arrange
        purchase = Purchase()
        # We make a for loop to check several inputs.
        purchase.phones.update(valid_phone_list)

        # Act
        purchase.buy()
        print(valid_phone_list)
        # Assert
        # We check if purchase.phones list is equal to the inputs.
        self.assertEqual(purchase.phones, valid_phone_list)

    # Test if a Purchase's price is updated - the price of the added phone should be added to the total price

    def test_get_price_after_selecting_phone__success(self):
        # Arrange
        phonesDict = {"Motorola G99": 800}
        purchase = Purchase()

        # Act
        purchase.get_price_after_selecting_phone(phonesDict, "Motorola G99")

        # Assert
        self.assertEqual(purchase.price, 800)

    # Test if a Purchase's price is updated - the test should fail since selected phone is not in the dictionary of available phones

    def test_get_price_after_selecting_phone__fail(self):
        # Arrange
        phonesDict = {"Motorola G99": 800}
        purchase = Purchase()

        # Assert
        self.assertRaises(
            ValueError, purchase.get_price_after_selecting_phone, phonesDict, "iPhone 99")

    # Test if a Purchase's price is updated - the total price should be decremented by the price of the selected phone
    def test_get_price_after_unselecting_phone__success(self):
        # Arrange
        purchase = Purchase()
        purchase.phones = {"Motorola G99": 800}
        purchase.price = 800

        # Act
        purchase.get_price_after_unselecting_phone("Motorola G99")

        # Assert
        self.assertEqual(purchase.price, 0)

    # Test if a Purchase's price is updated - the test should fail since selected phone is not in the dictionary of Purchase's phones
    def test_get_price_after_unselecting_phone__fail(self):
        # Arrange
        purchase = Purchase()
        purchase.phones = {"Motorola G99": 800}
        purchase.price = 800

        # Assert
        self.assertRaises(
            ValueError, purchase.get_price_after_unselecting_phone, "iPhone 99")
