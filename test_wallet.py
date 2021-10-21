import unittest
from wallet import Wallet



class TestWalletMoney(unittest.TestCase):
    """ Tests for instantiating a Wallet object, test that its money list has a len of 88"""


    def setUp(self):
        self.customer = Wallet()

   
    def __init__(self):
        """ Testing for instantiating a Wallet object, test that its money list has a len of 88 """
        money_list = len(self.customer.fill_wallet)
        self.assertEqual(len(self.money_list), money_list, '88')


if __name__ == '__main__':
    unittest.main()
