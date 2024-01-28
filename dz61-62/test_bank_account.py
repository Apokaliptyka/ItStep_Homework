from task52 import BankAccount

import unittest


class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.user1 = BankAccount("Megan", "12999", 1500, "USD")
        self.user2 = BankAccount("Alica", "12996", 1500, "USD")
        self.user3 = BankAccount("Tomas", "12347", 1500, "USD")

    def tearDown(self):
        del self.user1
        del self.user2
        del self.user3
        BankAccount.accounts.clear()

    def test_deposit(self):
        self.user1.deposit(500)
        self.assertEqual(self.user1._balance.amount, 2000)

    def test_withdraw(self):
        self.user1.withdraw(1000)
        self.assertEqual(self.user1._balance.amount, 500)

    def test_change_owner_name(self):
        self.user1.change_owner_name("Andrew")
        self.assertEqual(self.user1.owner_name, "Andrew")

    def test_transfer_funds(self):
        self.user1.transfer_funds(self.user2, 500)
        self.assertEqual(self.user1._balance.amount, 1000)
        self.assertEqual(self.user2._balance.amount, 2000)


if __name__ == "__main__":
    unittest.main()
