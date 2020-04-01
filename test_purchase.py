import unittest
from unittest_data_provider import data_provider
from purchase import Purchase


class test_purchase(unittest.TestCase):

    def valid_phone_lines(): return ((0,), (1,), (6,), (7,))

    # Test if number of phone lines and the price is incremented.
    # Data provider will feed valid upper boundary and valid lower boundary values
    @data_provider(valid_phone_lines)
    def test_increment_phonelines_success(self, valid_phone_lines):
        # Arrange
        purchase = Purchase()
        # Act
        purchase.phones_lines = valid_phone_lines
        initial_price = purchase.price
        purchase.increment_phonelines()
        print(valid_phone_lines)
        # Assert
        self.assertEqual(purchase.phones_lines, valid_phone_lines + 1)
        self.assertEqual(purchase.price, initial_price +
                         purchase.phone_lines_price)

    def invalid_phone_lines(): return ((9,), (8,), (2,), (1,))

    # Test if number of phone lines and the price is incremented.
    # Data provider will feed valid upper boundary and valid lower boundary values
    @data_provider(invalid_phone_lines)
    def test_decrement_phonelines_success(self, invalid_phone_lines):
        # Arrange
        purchase = Purchase()
        # Act
        # We test both the valid upper boundary and valid lower boundary
        # Data provider will feed the defined values here
        purchase.phones_lines = invalid_phone_lines
        initial_price = purchase.price
        purchase.decrement_phonelines()
        # Assert
        # We make sure that number of phone lines and the price has adjusted accordingly
        self.assertEqual(purchase.phones_lines, invalid_phone_lines - 1)
        self.assertEqual(purchase.price, initial_price -
                         purchase.phone_lines_price)

    # Test if incrementing the number of phone lines throws an error when it already has the upper boundary value.
    def test_increment_phonelines_fail(self):
        # Arrange
        purchase = Purchase()
        purchase.phones_lines = purchase.max_phone_lines

        # Act and Assert
        with self.assertRaises(ValueError):
            purchase.increment_phonelines()

    # Test if decrementing the number of phone lines throws an error when it already has the lower boundary value.
    def test_decrement_phonelines_fail(self):
        # Arrange
        purchase = Purchase()
        purchase.phones_lines = 0

        # Act and Assert
        with self.assertRaises(ValueError):
            purchase.decrement_phonelines()

    # Test if internet_connection boolean is changed to True as expected and price is adjusted accordingly.
    def test_internet_connection_True_and_check_price(self):
        # Arrange
        purchase = Purchase()
        initial_price = purchase.price
        purchase.internet_connection = True

        # Act
        purchase.change_internet_connection(purchase.internet_connection)

        # Assert
        self.assertTrue(purchase.internet_connection)
        self.assertEqual(purchase.price, initial_price + purchase.internet_connection_price)

    # Test if internet_connection boolean is changed to False as expected and price is adjusted accordingly.
    def test_internet_connection_False_and_check_price(self):
        # Arrange
        purchase = Purchase()
        initial_price = purchase.price
        purchase.internet_connection = False

        # Act
        purchase.change_internet_connection(purchase.internet_connection)

        # Assert
        self.assertFalse(
            purchase.change_internet_connection(purchase.internet_connection)
        )
        if initial_price == 0:
            self.assertEqual(purchase.price, 0)
        else:
            self.assertEqual(purchase.price, initial_price - purchase.internet_connection_price)

    # Test if an exception thrown when user tries to buy an empty list of phones.
    def test_buy_Fail(self):
        # Arrange
        purchase = Purchase()

        # Act
        with self.assertRaises(ValueError):
            purchase.buy()

        # Assert
        self.assertEqual(purchase.phones, {})

    def valid_phone_list(): return (({"Motorola G99": 800},), ({
        "iPhone 99": 6000},), ({"Samsung Galaxy 99": 1000},))

    # Test user can successfully but a basket with a valid input of phones.
    @data_provider(valid_phone_list)
    def test_buy_Success(self, valid_phone_list):
        # Arrange
        purchase = Purchase()
        purchase.phones.update(valid_phone_list)

        # Act
        purchase.buy()
        print(valid_phone_list)
        # Assert
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

    # Test if a Purchase's price is updated
    # The test should fail since selected phone is not in the dictionary of available phones

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

    # Test if a Purchase's price is updated
    # The test should fail since selected phone is not in the dictionary of Purchase's phones
    def test_get_price_after_unselecting_phone__fail(self):
        # Arrange
        purchase = Purchase()
        purchase.phones = {"Motorola G99": 800}
        purchase.price = 800

        # Assert
        self.assertRaises(
            ValueError, purchase.get_price_after_unselecting_phone, "iPhone 99")
