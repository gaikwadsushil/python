from banksystem import *

acc_type1 = AccType(1, "Savings Account")
acc_type2 = AccType(2, "Salary Account")
acc_type3 = AccType(3, "Current Account")
acc_type4 = AccType(4, "Fixed Deposit Account (FD)")
acc_type5 = AccType(5, "Recurring Deposit Account (RD)")
acc_type6 = AccType(6, "NRO Savings Account")
acc_type7 = AccType(7, "NRO Fixed Deposit Account (FD)")
acc_type8 = AccType(8, "NRE Savings Account")
acc_type9 = AccType(9, "NRE Fixed Deposit Account (FD)")
acc_type10 = AccType(10, "FCNR Account")


bank1 = Bank(1, "HDFC Bank", "HDFC", "Mumbai")
bank2 = Bank(2, "ICICI Bank", "ICICI", "Delhi")
bank3 = Bank(3, "SBI Bank", "SBI", "Chennai")


customer1 = Customer(1, "Rahul Sharma", "Mumbai", "9876543210")
customer2 = Customer(2, "Priya Patel", "Delhi", "9876543211")
customer3 = Customer(3, "Kumar Singh", "Chennai", "9876543212")
customer4 = Customer(4, "Neha Gupta", "Bangalore", "9876543213")
customer5 = Customer(5, "Rajesh Jain", "Kolkata", "9876543214")
customer6 = Customer(6, "Sushil Gaikwad", "Hyderabad", "9876543215")
customer7 = Customer(7, "Vishal Gaikwad", "Mumbai", "9876543216")


account1 = Account(101, 100000, acc_type1, bank1.bank_id)
account2 = Account(102, 200000, acc_type2, bank2.bank_id)
account3 = Account(103, 500000, acc_type3, bank3.bank_id)
account4 = Account(104, 1000200, acc_type4, bank1.bank_id)
account5 = Account(105, 2000000, acc_type5, bank2.bank_id)
account6 = Account(106, 5000000, acc_type6, bank3.bank_id)
account7 = Account(107, 4000000, acc_type7, bank1.bank_id)


account_customer1 = AccountCustomer(account1.account_no, customer1.custid)
account_customer2 = AccountCustomer(account2.account_no, customer2.custid)
account_customer3 = AccountCustomer(account3.account_no, customer3.custid)
account_customer4 = AccountCustomer(account4.account_no, customer4.custid)
account_customer5 = AccountCustomer(account5.account_no, customer5.custid)
account_customer6 = AccountCustomer(account6.account_no, customer6.custid)
account_customer7 = AccountCustomer(account7.account_no, customer7.custid)


loan1 = Loan(1, 5000000, 8.00, "home loan")
loan2 = Loan(2, 1000000, 12.00, "personal loan")
loan3 = Loan(3, 2000000, 10.50, "car loan")
loan4 = Loan(4, 500000, 9.00, "education loan")
loan5 = Loan(5, 10000000, 11.00, "business loan")
loan6 = Loan(6, 400000, 8.50, "gold loan")
loan7 = Loan(7, 6000000, 8.00, "home loan")


loan_interest1 = LoanInterest("Business Loan", 11.00)
loan_interest2 = LoanInterest("Car Loan", 12.00)
loan_interest3 = LoanInterest("education loan", 7.00)
loan_interest4 = LoanInterest("gold loan", 13.00)
loan_interest5 = LoanInterest("Home Loan", 8.00)
loan_interest6 = LoanInterest("Mortgage Loan", 9.00)
loan_interest7 = LoanInterest("Personal Loan", 10.00)


offer1 = Offer(1, loan1.loan_id, 5.00, "New Customer Offer", bank2.bank_id)
offer2 = Offer(2, loan2.loan_id, 3.50, "Referral Offer", bank1.bank_id)
offer3 = Offer(3, loan3.loan_id, 4.25, "Student Offer", bank3.bank_id)
offer4 = Offer(4, loan4.loan_id, 4.00, "Senior Citizen Offer", bank1.bank_id)
offer5 = Offer(5, loan5.loan_id, 3.75, "Employee Offer", bank2.bank_id)
offer6 = Offer(6, loan6.loan_id, 4.50, "Festival Offer", bank3.bank_id)


payment1 = Payment(1, loan1.loan_id, 100.00, "2022-01-01")
payment2 = Payment(2, loan1.loan_id, 200.00, "2022-02-01")
payment3 = Payment(3, loan2.loan_id, 50.00, "2022-03-01")
payment4 = Payment(4, loan7.loan_id, 300.00, "2023-10-01")


repayment1 = Repayment(1, customer1.custid, loan1.loan_id, 500, "2023-04-03")
repayment2 = Repayment(2, customer2.custid, loan2.loan_id, 250, "2023-04-08")
repayment3 = Repayment(3, customer3.custid, loan3.loan_id, 1000, "2023-04-13")


transaction1 = Transaction(1, customer1.custid, account1.account_no, 1000.00, "2023-04-01", "deposit")
transaction2 = Transaction(2, customer2.custid, account2.account_no, 500.00, "2023-04-05", "deposit")
transaction3 = Transaction(3, customer3.custid, account3.account_no, 2000.00, "2023-04-10", "deposit")
transaction4 = Transaction(4, customer4.custid, account4.account_no, 500.00, "2023-10-01", "deposit")
transaction5 = Transaction(5, customer1.custid, account1.account_no, 200.00, "2023-04-02", "withdrawal")
transaction6 = Transaction(6, customer2.custid, account2.account_no, 100.00, "2023-04-07", "withdrawal")
transaction7 = Transaction(7, customer3.custid, account3.account_no, 500.00, "2023-04-12", "withdrawal")
transaction8 = Transaction(8, customer4.custid, account4.account_no, 300.00, "2023-10-02", "withdrawal")


print(acc_type1)

print(bank1)

print(customer1)

print(account1)

print(account_customer1)

print(loan1)

print(loan_interest1)

print(offer1)

print(payment1)

print(repayment1)

print(transaction1)
