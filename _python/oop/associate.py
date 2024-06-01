from Bank_Account import Bank_Account
class User():
      def __init__(self,name,email):
        self.name = name
        self.email = email
        self.account = Bank_Account(int_rate=0.02, balance=0)	
      def make_deposit(self):
        self.account.deposit(100)
        return self
      def make_withdrawl(self):
         self.account.balance
         return self
      def diplay_user_balance(self):
         self.account.display_account_info()
         return self
      
            