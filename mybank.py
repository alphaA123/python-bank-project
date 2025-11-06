# def greeting(name):
#     print("Welcome" ,name,"May God bless you with Abundance");
#     return True

# greeting('Abhishek');

# class Employee:
#     #Initialise object
#     def __init__(self,name,position,salary):
#         self.name=name
#         self.position=position
#         self.salary=salary
#     #method
#     def display_info(self):
#         return f'Mr. {self.name} is a {self.position} with salary {self.salary}'
    
# #creating an object
# employee1=Employee('Abhishek Kumar','Data Engineer','2500000');

# print(employee1.display_info());
# employee1.salary=25000000;
# print(employee1.display_info());

class BankAccount:
    def __init__(self,account_id,balance=1000):
        self.account_id=account_id
        self.balance=balance

    def deposit(self,amount):
        if(amount>0):
            self.balance+=amount
            return f"Deposit of ${amount} successful. 🤑"
        else:
            return "Invalid Deposit Amount"
        
    def withdraw(self,wamount):
        if(wamount>0):
            self.balance-=wamount
            return f"Withdrawal of ${wamount} successful.😞"
        else:
            return "Invalid Deposit Amount"
        
    def get_balance(self):
        return self.balance;


# Global dictionary to store all BankAccount objects
accounts={}
def for_deposit(account_id,amount):
    print("Welcome to AU Cooperative Bank");
    if account_id not in accounts:
        print(f"{account_id} is not present. Creating a new account with default balance..😀")
    accounts[account_id]=BankAccount(account_id)

    account=accounts[account_id]

    print(account.deposit(amount))
    return account.get_balance();

def for_withdrawal(account_id,amount):
    print("Welcome to AU Cooperative Bank");
    if account_id not in accounts:
        print(f"{account_id} doesn't exist. Please create a new account..😒")
        return False

    account=accounts[account_id]

    print(account.withdraw(amount))
    return account.get_balance();

# Deposit $500 into account 'A101'
user1=for_deposit('A101',500);
print(f"Account A101 balance after deposit: ${user1}");

user2=for_withdrawal('A101',500);
print(f"Account A101 balance after Withdrawal: ${user2}");


