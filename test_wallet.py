import unittest
import wallet
import customer


class TestWalletMoney(unittest.TestCase):
    """ Tests for instantiating a Wallet object, test that its money list has a len of 88"""


    def setUp(self):
        self.customer = wallet()

    def test_instan_wallet_object(self):






# Wallet class:
# 1. fill_wallet
# a. Instantiate a Wallet object, test that its money list has a len of 88