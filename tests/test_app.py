import unittest
from Purchase import Purchase
from Phone import Phone


class TestEmployee(unittest.TestCase):
    def setUp(self):
        print('setUp')
        self.mySecondPurchase = Purchase()
        self.mySecondPurchase.phones_lines = 3
        self.mySecondPurchase.internet_connection = True
        self.mySecondPurchase.price = 0

    def test_increment_phonelines_success(self):
        self.mySecondPurchase.increment_phonelines()
        self.assertEqual(self.mySecondPurchase.phones_lines, 4)

    def test_decrement_phonelines_success(self):
        self.mySecondPurchase.decrement_phonelines()
        self.assertEqual(self.mySecondPurchase.phones_lines, 2)

    def test_increment_phonelines_fail(self):
        self.mySecondPurchase.phones_lines = 8

        with self.assertRaises(ValueError):
            self.mySecondPurchase.increment_phonelines()

    def test_decrement_phonelines_fail(self):
        self.mySecondPurchase.phones_lines = 0
        with self.assertRaises(ValueError):
            self.mySecondPurchase.decrement_phonelines()

    def test_internet_connection_True_and_check_price(self):
        # We call on the function mySecondPurchase.change_internet_connection.
        # The function takes 1 boolean parameter.
        # We insert self.mySecondPurchase.internet_connection which is supposed to be True.
        self.mySecondPurchase.change_internet_connection(self.mySecondPurchase.internet_connection)
        self.assertTrue(self.mySecondPurchase.internet_connection)
        # If the self.mySecondPurchase.internet_connection is True.
        # Then the self.mySecondPurchase.price should be equal to 200.
        self.assertEqual(self.mySecondPurchase.price, 200)
    

    def test_internet_connection_False_and_check_price(self):
        # We set self.mySecondPurchase.internet_connection to be False.
        self.mySecondPurchase.internet_connection = False
        # We check if mySecondPurchase.change_internet_connection(self.mySecondPurchase.internet_connection) is False. 
        self.assertFalse(self.mySecondPurchase.change_internet_connection(self.mySecondPurchase.internet_connection))
        # If it is False then mySecondPurchase.price should be equal 0.
        self.assertEqual(self.mySecondPurchase.price, 0)

    def test_buy_Fail(self):
        # We check if mySecondPurchase.price is equal to 0.
        self.assertEqual(self.mySecondPurchase.price, 0)
        # If it is then an error message will appear.
        with self.assertRaises(ValueError):
            self.mySecondPurchase.buy()


    def test_buy_Success(self):
        # We set mySecondPurchase.price to 1,2 and 3 in a for loop.
        for x in [1,2,3]:
            self.mySecondPurchase.price = x
            self.mySecondPurchase.buy()
            # We check if self.mySecondPurchase.price is greater than 0.
            self.assertGreater(self.mySecondPurchase.price, 0)

        