# test_mybank.py

import unittest
# Import the class you want to test from your main file
from mybank import BankAccount 

class TestBankAccount(unittest.TestCase):

    def test_initial_balance(self):
        # Test 1: Check if the default balance is set correctly
        account = BankAccount(account_id='T001')
        self.assertEqual(account.get_balance(), 1000)

    def test_deposit_positive(self):
        # Test 2: Check a successful positive deposit
        account = BankAccount(account_id='T002', balance=500)
        account.deposit(250)
        self.assertEqual(account.get_balance(), 750)

    def test_deposit_zero_or_negative(self):
        # Test 3: Check that a negative or zero deposit doesn't change the balance
        account = BankAccount(account_id='T003', balance=1000)
        
        # Attempt to deposit 0
        account.deposit(0)
        self.assertEqual(account.get_balance(), 1000)
        
        # Attempt to deposit a negative number
        account.deposit(-50)
        self.assertEqual(account.get_balance(), 1000)

# This allows the tests to be run directly when the file is executed
if __name__ == '__main__':
    unittest.main()