from peewee import *
from datetime import date
from tabulate import tabulate

mysql_db = MySQLDatabase(
    'pet_project',  # database name
    user='root',  # user name
    password='root',  # password
    host='localhost'  # hostname -> localhost or 127.0.0.1
)


class BaseModel(Model):
    class Meta:
        database = mysql_db


# Define table
class Bank(BaseModel):
    id = PrimaryKeyField(null=False)
    name = CharField(max_length=255)
    address = CharField(max_length=255)
    number = IntegerField()


class Customer(BaseModel):
    id = PrimaryKeyField(null=False)
    bank = ForeignKeyField(Bank, related_name='bank_id')
    clientName = CharField(max_length=255)
    clientAddress = CharField(max_length=255)
    dob = DateField()
    SSN = IntegerField(unique=True)
    phoneNumber = IntegerField()
    email = CharField(max_length=255)


class Account(BaseModel):
    Id = PrimaryKeyField(null=False)
    client = ForeignKeyField(Customer, related_name='client_id')
    accountNo = IntegerField(unique=True)
    balance = FloatField(default=0.00)


class Transactions(BaseModel):
    Id = PrimaryKeyField(null=False)
    accountDetails = ForeignKeyField(Account, related_name='account_id')
    transactionDate = DateField(default=str(date.today()))
    transactionType = CharField(max_length=255)
    transactionAmount = FloatField()


mysql_db.create_tables([Bank, Customer, Account, Transactions])


def findCustomer(SSN):
    try:
        searchBySsn = Customer.get(Customer.SSN == SSN)
    except Customer.DoesNotExist:
        searchBySsn = None
    return searchBySsn


# print(findCustomer(111451122))


def insertCustomer(clientNameParam, clientAddressParam, dobParam, SSNParam, phoneNumberParam, emailParam,
                   accountNoParam):
    existingBank = Bank.get(Bank.name == "Lena's Bank")
    customer = Customer(bank=existingBank, clientName=clientNameParam, clientAddress=clientAddressParam,
                        dob=dobParam, SSN=SSNParam, phoneNumber=phoneNumberParam, email=emailParam)
    new_account = Account(client=customer, accountNo=accountNoParam)
    customer.save()
    new_account.save()


def updateCustomer(clientNameParam, clientAddressParam, dobParam, SSNParam, phoneNumberParam, emailParam,
                   accountNoParam):
    existingBank = Bank.get(Bank.name == "Lena's Bank")
    customer = Customer(bank=existingBank, clientName=clientNameParam, clientAddress=clientAddressParam,
                        dob=dobParam, SSN=SSNParam, phoneNumber=phoneNumberParam, email=emailParam)
    new_account = Account(client=customer, accountNo=accountNoParam)
    customer.save()
    new_account.save()


def updateCustomerInfo(updatedCustomer):
    updatedCustomer.save()


def deleteCustomer(SSNParam):
    remove_q = Customer.get(Customer.SSN == SSNParam)
    remove_q.delete_instance(recursive=True)


# deleteCustomer(222451122)

# remove_q = Customer.delete().where(Customer.SSN == SSNParam)
# remove_q.execute()

# To get a list of names of all Bank customers
def listofBankClients():
    clientquery = Customer.select()
    for client in clientquery:
        print(tabulate([[client.clientName]], ["Name"], tablefmt="fancy_grid"))
        # print(client.clientName)


# listofBankClients()


def insertIntoDb():
    row = Bank(name="Lena's Bank", address="555 5th Ave, NY NY 10025", number=2125551155)
    row.save()


def addNewTransaction(accountNo, transactionTypeParam, transactionAmountParam):
    account1 = Account.get(Account.accountNo == accountNo)
    newTrans = Transactions(transactionType=transactionTypeParam,
                            transactionAmount=transactionAmountParam,
                            accountDetails=account1)
    account1.balance = account1.balance + float(transactionAmountParam)
    account1.save()
    newTrans.save()


def checkBalance(accountNo):
    try:
        account1 = Account.get(Account.accountNo == accountNo)
    except Account.DoesNotExist:
        print("\nAccount not found")
        return
    return account1.balance


# checkBalance(1000002311)


# query = Transactions.select(
# Transactions.transactionAmount,
# fn.SUM(Transactions.transactionAmount).alias('total')). \
# where(Transactions.accountDetails == account1)
# return query[0].total


def ShowTransactions(accountNo):
    account1 = Account.get(Account.accountNo == accountNo)
    tran_query = Transactions.select().where(Transactions.accountDetails == account1)

    # to print all transactions for given acct. number
    for transaction in tran_query:
        print(tabulate([["Transaction Id ", transaction.Id], ["Transaction Date ", transaction.transactionDate],
                        ["Transaction Type ", transaction.transactionType],
                        ["Transaction Amount ", transaction.transactionAmount]],
                       tablefmt="fancy_grid"))


# ShowTransactions(1000002311)

def openNewAccount(SSN, accountNoParam):
    customer = findCustomer(SSN)
    new_account = Account(client=customer, accountNo=accountNoParam)
    new_account.save()


# openNewAccount()

def closeExistingAccount(accountNumParam):
    try:
        removeacct = Account.get(Account.accountNo == accountNumParam)
        removeacct.delete_instance(recursive=True)
    except Account.DoesNotExist:
        print("\nAccount not found")
        return
    print("\nAccount number " + accountNumParam + " has been removed")

# closeExistingAccount(1122334499)

# print(checkBalance(1000002322))


# insertIntoDb()
# insertCustomer(clientNameParam = "John Snow", clientAddressParam = "The Wall", dobParam = 1980-01-22,
# SSNParam = 999007676, phoneNumberParam = 2129990077, emailParam = "j.snow1@yahoo.com",
# accountNoParam = 1000004413)
# addNewTransaction(1000002311,"Deposit",100.00)
# addNewTransaction(1000002322,"Deposit", 10.50)

#### to do ####
# 1. Create search for client in "generalClientInfo" by client's name OR SSN - N/A
# 2. "on delete" cascade for each Foreign Key
# 3. One-liner for func listofBankClients() #print(client.clientName for client in clientquery)
# 4. Account types (Checking, SV, Loan)
