import unittest
from soda_machine import SodaMachine


class TestFillRegister(unittest.TestCase):
    """ Tests for instantiating a SodaMachine object, test that its register list has a len of 88 """


    def setUp(self):
        self.soda_machine = SodaMachine()

    def test_fill_register(Self):
        """ Tests for instantiating a SodaMachine object, test that its register list has a len of 88 """
        fill_register = SodaMachine()

        def __init__
        fill_up_register = len(self.soda_machine.fill_register)



    # def fill_register(self):
    #     """Method will fill SodaMachine's register with certain amounts of each coin when called."""
    #     for index in range(8):
    #         self.register.append(coins.Quarter())
    #     for index in range(10):
    #         self.register.append(coins.Dime())
    #     for index in range(20):
    #         self.register.append(coins.Nickel())
    #     for index in range(50):
    #         self.register.append(coins.Penny())


# def test_add_can_to_backpack(self):
#     """ Tests passing in cola object to test length of backpack """
#     cola = Cola()
#     length_of_backpack = len(self.customer.backpack.purchased_cans)
#     self.customer.add_can_to_backpack(cola)
#     self.assertEqual(len(self.customer.backpack.purchased_cans), length_of_backpack +1)



# Soda Machine class:
# 1. fill_register – 1 test
# a.    Instantiate a SodaMachine object, test that its register list has a len of 88
# 
# 2. fill_inventory- 1 test
# a.    Instantiate a SodaMachine object, test that its inventory list has a len of 30
# 
# 3. get_coin_from_register- 5 tests
# a.    Test each type of coin can be returned from register
# b.    Test that passing in a string that is not a valid coin name will return None
# 
# 4. register_has_coin - 5 tests
# a.    Test that each type of coin will return True
# b.    est that a non-valid coin name will return False
# 
# 5. determine_change_value – 3 tests
# a.    Test with total payment higher
# b.    Test with select_soda_price higher
# c.    Test with two equal values
# 
# 6. calculate_coin_value - 2 tests
# a.    Instantiate each of the 4 coin types and append them to a list. Pass the list into this
#       function, ensure the returned values is .41
# b.    Pass in an empty list. Ensure the returned value is 0.
# 
# 7. get_inventory_soda - 4 tests
# a.    Pass in each of the 3 soda names, ensure the returned can has the same name
# b.    Pass in “Mountain Dew” and ensure None is returned
# 
# 8. return_inventory - 1 test
# a.    Instantiate a can and pass it into the method. Test that the len of self.inventory is now
#       31
# 
# 9. deposit_coins_into_register - 1 test
# a.    Instantiate each of the 4 coins and append them to a list. Pass the list into the function,
# ensure the len of self.register is 92