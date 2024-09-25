class account:
    def __init__(self, account_no, balance, acc_type):
        self.account_no = account_no
        print(f"Account number {account_no} added")
        self.balance = balance
        print(f"Initial balance is {balance}")
        self.acc_type = acc_type
        print(f"Account type is {acc_type}")
        
    def greet(self):
        print("Hello, welcome to our bank")


account1 = account("101",100000, "savings")

account1.greet()

class customer:
    def __init__(self, custid, name, address, phone):
        self.custid = custid
        print(f"customer id {custid} added")
        self.name = name
        print(f"Customer name is {name}")
        self.address = address
        print(f"Customer address is {address}")
        self.phone = phone
        print(f"Customer phonenumber is {phone}")


    def greet(self):
        print("Thank you for be over customer")


customer1 = customer("1","Rahul Sharma", "Mumbai", 9876543210)

customer1.greet()


class transaction:
    def __init__(self, transaction_id, custid, account_id, amount, date, transaction_type):
        self.transaction = transaction_id
        print(f"Transaction id {transaction_id} added")
        self.custid = custid
        print(f"Customer id is {custid}")
        self.account = account_id
        print(f"Account id is {account_id}")
        self.amount = amount
        print(f"Transaction amount is {amount}")
        self.date = date
        print(f"Transaction date is {date}")
        self.transaction_type = transaction_type
        print(f"Transaction type is {transaction_type}")

    def greet(self):
      print("Transaction done successfully")

transaction1 = transaction("1","1","101",1000,"2023-04-01", "deposit")

transaction1.greet()

