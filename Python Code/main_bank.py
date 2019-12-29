from enum import Enum

from consolemenu import *
from consolemenu.items import *
import models as models
from tabulate import tabulate


def list_of_all_customers():
    models.list_of_bank_customers()


def find_customer():
    ssn = input("Please enter Customer's SSN: ")
    existing_customer = models.find_customer(ssn)
    if existing_customer is not None:
        print("\nInfo for customer " + existing_customer.name + " is below: ")
        print(tabulate([["Customer's Id  ", existing_customer.Id], ["Customer's name ", existing_customer.name],
                        ["Customer's Address ", existing_customer.address],
                        ["Customer's Date of Birth ", existing_customer.dob],
                        ["Customer's SSN ", existing_customer.ssn],
                        ["Customer's phone Number ", existing_customer.phone_number],
                        ["Customer's email ", existing_customer.email]], tablefmt="fancy_grid"))


def update_customer():
    ssn = input("Please enter customer's SSN: ")
    existing_customer = models.find_customer(ssn)
    if existing_customer is None:
        return

    print("Existing Customer Current Name: " + existing_customer.name)

    new_customer_name = str(input("Please enter customer's new name, otherwise hit 'Enter': "))
    if new_customer_name:
        existing_customer.name = new_customer_name

    new_customer_address = str(input("Please enter customer's new address, otherwise hit 'Enter': "))
    if new_customer_address:
        existing_customer.address = new_customer_address

    new_customer_dob = input("Please enter customer's new Date of Birth (YYYY-MM-DD), otherwise hit 'Enter': ")
    if new_customer_dob:
        existing_customer.dob = new_customer_dob

    new_customer_ssn = input("Please enter customer's new SSN, otherwise hit 'Enter': ")
    if new_customer_ssn:
        existing_customer.SSN = new_customer_ssn

    new_customer_phone_no = str(input("Please enter customer's new phone number, otherwise hit 'Enter': "))
    if new_customer_phone_no:
        existing_customer.phoneNumber = new_customer_phone_no

    new_customer_email = str(input("Please enter customer's new email, otherwise hit 'Enter': "))
    if new_customer_email:
        existing_customer.email = new_customer_email

    models.update_customer_info(existing_customer)
    print("\nCustomer's profile has been updated")


def remove_customer():
    ssn = input("Please enter customer's SSN: ")
    existing_customer = models.find_customer(ssn)
    if existing_customer is not None:
        models.delete_customer(existing_customer)
        print("Customer " + existing_customer.name + " is deleted")


def add_new_customer():
    new_customer_name = str(input("Please enter customer's name (First name Last name), then hit 'Enter': "))
    new_customer_address = str(input("Please enter customer's address, then hit 'Enter': "))
    new_customer_dob = input("Please enter customer's Date of Birth (YYYY-MM-DD), then hit 'Enter': ")
    new_customer_ssn = input("Please enter customer's SSN, then hit 'Enter': ")
    new_customer_phone_no = str(input("Please enter customer's phone number, then hit 'Enter': "))
    new_customer_email = str(input("Please enter customer's email, then hit 'Enter': "))
    new_customer_no = input("Please enter customer's 10-digit account number, then hit 'Enter': ")
    new_customer_type = str(input("Please enter type of account (Checking, Savings, Loan), then hit 'Enter': "))
    if acct_type_validation(new_customer_type):
        models.insert_customer(name_param=new_customer_name, address_param=new_customer_address,
                               dob_param=new_customer_dob, ssn_param=new_customer_ssn,
                               phone_number_param=new_customer_phone_no, email_param=new_customer_email,
                               account_no_param=new_customer_no, account_type_param=new_customer_type)
        print("\nNew customer " + new_customer_name + " has been added. Please verify the following info: ")
        print(tabulate([["Name ", new_customer_name], ["Address ", new_customer_address], ["Date of Birth ", new_customer_dob],
                        ["SSN ", new_customer_ssn], ["Phone Number ", new_customer_phone_no],
                        ["Email ", new_customer_email], ["Account number ", new_customer_no], ["Type ", new_customer_type]],
                       tablefmt="fancy_grid"))


def get_balance():
    account_no = input("Please enter customer's 10-digit account number, then hit 'Enter': ")
    existing_acct_balance = models.check_balance(account_no)
    if existing_acct_balance is not None:
        print("\nAccount balance: $" + str(existing_acct_balance))


def open_new_account():
    ssn = input("Please enter customer's SSN: ")
    existing_customer = models.find_customer(ssn)
    if existing_customer is not None:
        new_account_no = input("Please enter new 10-digit account number, then hit 'Enter': ")
        new_account_type = str(input("Please enter type of account (Checking, Savings, Loan), then hit 'Enter': "))
        if acct_type_validation(new_account_type):
            models.open_new_account(existing_customer, account_no_param=new_account_no,
                                    account_type_param=new_account_type)
            print("\nNew account number " + str(new_account_no) + " has been added to customer's profile")


def acct_type_validation(new_account_type):
    if new_account_type in AccountType._value2member_map_:
        return True
    print("Invalid entry. Please enter valid account type")
    return False


def close_account():
    account_no = input("Please enter customer's 10-digit account number that you wish to delete, then hit 'Enter': ")
    models.close_existing_account(account_num_param=account_no)


def add_new_transaction():
    account_no = input("Please enter customer's 10-digit account number, then hit 'Enter': ")
    existing_account = models.get_account(account_no)
    if existing_account is None:
        return
    transaction_type = str(input("Please enter type of transaction (Deposit, Withdrawal, Interest, Payment): "))
    transaction_amount = input("Please enter transaction amount ('+' or '-'): ")
    models.add_new_transaction(account_no_param=account_no, transaction_type_param=transaction_type,
                               transaction_amount_param=transaction_amount)
    print("\n" + transaction_type + " transaction for $" + str(transaction_amount) +
          " has been added. Please verify transaction details below: ")
    print(tabulate([["Account Number ", account_no], ["Type ", transaction_type], ["Amount ", transaction_amount]],
                   tablefmt="fancy_grid"))


def transaction_history():
    account_no = input("Please enter customer's 10-digit account number, then hit 'Enter': ")
    models.show_transactions(account_no=account_no)


def main():
    # Create the menu
    menu = ConsoleMenu("Lena's Bank main menu", "Welcome to Lena's Bank! Please select from the following menu:")

    # A FunctionItem runs a Python function when selected
    list_of_all_customers_function = FunctionItem("List of all customers", list_of_all_customers)
    find_customer_function = FunctionItem("Find customer by SSN", find_customer)
    update_customer_info_function = FunctionItem("Update customer info", update_customer)
    remove_customer_function = FunctionItem("Remove customer", remove_customer)
    add_new_customer_function = FunctionItem("Add new customer", add_new_customer)

    get_balance_function = FunctionItem("Get balance", get_balance)
    open_new_account_function = FunctionItem("Open New Account", open_new_account)
    close_account_function = FunctionItem("Close account", close_account)

    add_new_transaction_function = FunctionItem("Add new transaction", add_new_transaction)
    view_transaction_history_function = FunctionItem("View transaction history", transaction_history)

    list_of_all_customers_submenu_item = SelectionMenu([])
    list_of_all_customers_submenu_item.append_item(list_of_all_customers_function)
    list_of_all_customers_submenu_item.append_item(find_customer_function)
    list_of_all_customers_submenu_item.append_item(update_customer_info_function)
    list_of_all_customers_submenu_item.append_item(add_new_customer_function)
    list_of_all_customers_submenu_item.append_item(remove_customer_function)

    work_with_accounts_selection_menu = SelectionMenu([])
    work_with_accounts_selection_menu.append_item(get_balance_function)
    work_with_accounts_selection_menu.append_item(open_new_account_function)
    work_with_accounts_selection_menu.append_item(close_account_function)

    process_transactions_selection_menu = SelectionMenu([])
    process_transactions_selection_menu.append_item(add_new_transaction_function)
    process_transactions_selection_menu.append_item(view_transaction_history_function)

    manage_customers_submenu_item = SubmenuItem("Manage customers", list_of_all_customers_submenu_item, menu)

    accounts_submenu_item = SubmenuItem("Work with accounts", work_with_accounts_selection_menu, menu)
    process_transactions_submenu_item = SubmenuItem("Process Transactions", process_transactions_selection_menu, menu)

    menu.append_item(manage_customers_submenu_item)
    menu.append_item(accounts_submenu_item)
    menu.append_item(process_transactions_submenu_item)

    models.create_lenas_bank()
    menu.show()


class AccountType(Enum):
    CHECKING = "Checking"
    SAVINGS = "Savings"
    LOAN = "Loan"


if __name__ == "__main__":
    main()