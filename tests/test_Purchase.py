import unittest
from Purchase import Purchase


class TestEmployee(unittest.TestCase):
    def setUp(self):
        print("setUp")
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

    def test_internet_connection_success(self):
        self.mySecondPurchase.internet_connection()
        self.assertTrue(self.mySecondPurchase.internet_connection == True)
        self.assertEqual(self.mySecondPurchase.price, 200)

    # def test_internet_connection_success(self):
    #     self.mySecondPurchase.internet_connection(self.mySecondPurchase.internet_connection)
    #     self.assertFalse(self.mySecondPurchase.internet_connection)
