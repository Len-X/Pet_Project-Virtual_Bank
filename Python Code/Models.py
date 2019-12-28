from peewee import *
from datetime import date
from tabulate import tabulate

bank_name = "Lena's Bank"
bank_address = "555 5th Ave, NY NY 10025"
bank_number = 2125551155

mysql_db = MySQLDatabase(
    'pet_project',  # database name
    user='root',  # user name
    password='root',  # password
    host='localhost'  # hostname -> localhost or 127.0.0.1
)
#mysql_db.default_values_insert()


class BaseModel(Model):
    class Meta:
        database = mysql_db


class Bank(BaseModel):
    Id = PrimaryKeyField(null=False)
    name = CharField(max_length=255)
    address = CharField(max_length=255)
    number = IntegerField()


class Customer(BaseModel):
    Id = PrimaryKeyField(null=False)
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
    accountType = CharField(max_length=255)
    balance = FloatField(default=0.00)


class Transactions(BaseModel):
    Id = PrimaryKeyField(null=False)
    accountDetails = ForeignKeyField(Account, related_name='account_id')
    transactionDate = DateField(default=str(date.today()))
    transactionType = CharField(max_length=255)
    transactionAmount = FloatField()


mysql_db.create_tables([Bank, Customer, Account, Transactions])


def create_lenas_bank():
    bank = Bank.get_or_none(number=bank_number)
    if bank is None:
        Bank.create(name=bank_name, address=bank_address, number=bank_number)


def find_customer(ssn):
    try:
        customer_by_ssn = Customer.get(Customer.SSN == ssn)
    except Customer.DoesNotExist:
        print("Client Not Found")
        return None
    return customer_by_ssn


def insert_customer(client_name_param, client_address_param, dob_param, ssn_param, phone_number_param, email_param,
                    account_no_param):
    existing_bank = Bank.get(Bank.number == bank_number)
    customer = Customer(bank=existing_bank, clientName=client_name_param, clientAddress=client_address_param,
                        dob=dob_param, SSN=ssn_param, phoneNumber=phone_number_param, email=email_param)
    new_account = Account(client=customer, accountNo=account_no_param)
    customer.save()
    new_account.save()


def update_customer_info(customer_to_update):
    customer_to_update.save()


def delete_customer(customer_to_remove):
    customer_to_remove.delete_instance(recursive=True)


# To get a list of names of all Bank customers
def list_of_bank_clients():
    client_query = Customer.select()
    print("List of bank clients:\n")
    for client in client_query:
        print(client.clientName)


def add_new_transaction(account_no_param, transaction_type_param, transaction_amount_param):
    existing_account = get_account(account_no_param)
    if existing_account is not None:
        new_trans = Transactions(transactionType=transaction_type_param,
                                 transactionAmount=transaction_amount_param,
                                 accountDetails=existing_account)
        existing_account.balance = existing_account.balance + float(transaction_amount_param)
        existing_account.save()
        new_trans.save()


def check_balance(account_no):
    existing_account = get_account(account_no)
    if existing_account is None:
        return None
    return existing_account.balance


def show_transactions(account_no):
    find_account = Account.get(Account.accountNo == account_no)
    transactions_query = Transactions.select().where(Transactions.accountDetails == find_account)

    # to print all transactions for given acct. number
    for transaction in transactions_query:
        print(tabulate([["Transaction Id ", transaction.Id], ["Transaction Date ", transaction.transactionDate],
                        ["Transaction Type ", transaction.transactionType],
                        ["Transaction Amount ", transaction.transactionAmount]],
                       tablefmt="fancy_grid"))


def open_new_account(existing_customer, account_no_param, account_type_param):
    new_account = Account(client=existing_customer, accountNo=account_no_param, accountType=account_type_param)
    new_account.save()


def get_account(account_num_param):
    try:
        existing_account = Account.get(Account.accountNo == account_num_param)
    except Account.DoesNotExist:
        print("\nAccount not found")
        return None
    return existing_account


def close_existing_account(account_num_param):
    account_to_remove = get_account(account_num_param)
    if account_to_remove is not None:
        account_to_remove.delete_instance(recursive=True)
        print("\nAccount number " + account_num_param + " has been removed")
