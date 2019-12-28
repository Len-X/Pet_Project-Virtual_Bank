from enum import Enum

from consolemenu import *
from consolemenu.items import *
import Models as models
from tabulate import tabulate


def list_of_all_clients():
    models.list_of_bank_clients()


def find_customer():
    ssn = input("Please enter client's SSN: ")
    existing_customer = models.find_customer(ssn)
    if existing_customer is not None:
        print("\nInfo for client " + existing_customer.clientName + " is below: ")
        print(tabulate([["Client's Id ", existing_customer.id], ["Client's name ", existing_customer.clientName],
                        ["Client's Address ", existing_customer.clientAddress],
                        ["Client's Date of Birth ", existing_customer.dob],
                        ["Client's SSN ", existing_customer.SSN],
                        ["Client's phone Number ", existing_customer.phoneNumber],
                        ["Client's email ", existing_customer.email]], tablefmt="fancy_grid"))


def update_client():
    ssn = input("Please enter client's SSN: ")
    founded_customer = models.find_customer(ssn)
    if founded_customer is None:
        return

    print("Existing Customer Current Name: " + founded_customer.clientName)

    new_client_name = str(input("Please enter client's new name, otherwise hit 'Enter': "))
    if new_client_name:
        founded_customer.clientName = new_client_name

    new_client_address = str(input("Please enter client's new address, otherwise hit 'Enter': "))
    if new_client_address:
        founded_customer.clientAddress = new_client_address

    new_client_dob = input("Please enter client's new Date of Birth (YYYY-MM-DD), otherwise hit 'Enter': ")
    if new_client_dob:
        founded_customer.dob = new_client_dob

    new_client_ssn = input("Please enter client's new SSN, otherwise hit 'Enter': ")
    if new_client_ssn:
        founded_customer.SSN = new_client_ssn

    new_client_phone_no = str(input("Please enter client's new phone number, otherwise hit 'Enter': "))
    if new_client_phone_no:
        founded_customer.phoneNumber = new_client_phone_no

    new_client_email = str(input("Please enter client's new email, otherwise hit 'Enter': "))
    if new_client_email:
        founded_customer.email = new_client_email

    models.update_customer_info(founded_customer)


def remove_client():
    ssn = input("Please enter client's SSN: ")
    existing_customer = models.find_customer(ssn)
    if existing_customer is not None:
        models.delete_customer(existing_customer)
        print("Client " + existing_customer.clientName + " is deleted")


def add_new_client():
    new_client_name = str(input("Please enter client's name (First name Last name), then hit 'Enter': "))
    new_client_address = str(input("Please enter client's address, then hit 'Enter': "))
    new_client_dob = input("Please enter client's Date of Birth (YYYY-MM-DD), then hit 'Enter': ")
    new_client_ssn = input("Please enter client's SSN, then hit 'Enter': ")
    new_client_phone_no = str(input("Please enter client's phone number, then hit 'Enter': "))
    new_clients_email = str(input("Please enter client's email, then hit 'Enter': "))
    new_account_no = input("Please enter client's 10-digit account number, then hit 'Enter': ")
    new_account_type = str(input("Please enter type of account (Checking, Savings, Loan), then hit 'Enter': "))
    if acct_type_validation(new_account_type):
        models.insert_customer(client_name_param=new_client_name, client_address_param=new_client_address,
                               dob_param=new_client_dob, ssn_param=new_client_ssn,
                               phone_number_param=new_client_phone_no, email_param=new_clients_email,
                               account_no_param=new_account_no, account_type_param=new_account_type)
        print("\nNew client " + new_client_name + " has been added. Please verify the following info: ")
        print(tabulate([["Name ", new_client_name], ["Address ", new_client_address], ["Date of Birth ", new_client_dob],
                        ["SSN ", new_client_ssn], ["Phone Number ", new_client_phone_no],
                        ["Email ", new_clients_email], ["Account number ", new_account_no], ["Type ", new_account_type]],
                       tablefmt="fancy_grid"))


def get_balance():
    account_no = input("Please enter client's 10-digit account number, then hit 'Enter': ")
    existing_acct_balance = models.check_balance(account_no)
    if existing_acct_balance is not None:
        print("\nAccount balance: $" + str(existing_acct_balance))


def open_new_account():
    ssn = input("Please enter client's SSN: ")
    existing_customer = models.find_customer(ssn)
    if existing_customer is not None:
        new_account_no = input("Please enter new 10-digit account number, then hit 'Enter': ")
        new_account_type = str(input("Please enter type of account (Checking, Savings, Loan), then hit 'Enter': "))
        if acct_type_validation(new_account_type):
            models.open_new_account(existing_customer, account_no_param=new_account_no,
                                    account_type_param=new_account_type)
            print("\nNew account number " + new_account_no + " has been added to client's profile")


def acct_type_validation(new_account_type):
    if new_account_type in AccountType._value2member_map_:
        return True
    print("Invalid entry. Please enter valid account type")
    return False


def close_account():
    account_no = input("Please enter client's 10-digit account number that you wish to delete, then hit 'Enter': ")
    models.close_existing_account(account_num_param=account_no)


def add_new_transaction():
    account_no = input("Please enter client's 10-digit account number, then hit 'Enter': ")
    existing_account = models.get_account(account_no)
    if existing_account is None:
        return
    transaction_type = str(input("Please enter type of transaction (Deposit, Withdrawal, Interest, Payment): "))
    transaction_amount = input("Please enter transaction amount ('+' or '-'): ")
    models.add_new_transaction(account_no_param=account_no, transaction_type_param=transaction_type,
                               transaction_amount_param=transaction_amount)
    print("\n" + transaction_type + " transaction for $" + transaction_amount +
          " has been added. Please verify transaction details below: ")
    print(tabulate([["Account Number ", account_no], ["Type ", transaction_type], ["Amount ", transaction_amount]],
                   tablefmt="fancy_grid"))


def transaction_history():
    account_no = input("Please enter client's 10-digit account number, then hit 'Enter': ")
    models.show_transactions(account_no=account_no)


def main():
    # Create the menu
    menu = ConsoleMenu("Lena's Bank main menu", "Welcome to Lena's Bank! Please select from the following menu:")

    # A FunctionItem runs a Python function when selected
    list_of_all_clients_function = FunctionItem("List of all clients", list_of_all_clients)
    find_customer_function = FunctionItem("Find customer by SSN", find_customer)
    update_client_info_function = FunctionItem("Update client info", update_client)
    remove_client_function = FunctionItem("Remove client", remove_client)
    add_new_client_function = FunctionItem("Add new client", add_new_client)

    get_balance_function = FunctionItem("Get balance", get_balance)
    open_new_account_function = FunctionItem("Open New Account", open_new_account)
    close_account_function = FunctionItem("Close account", close_account)

    add_new_transaction_function = FunctionItem("Add new transaction", add_new_transaction)
    view_transaction_history_function = FunctionItem("View transaction history", transaction_history)

    list_of_all_clients_submenu_item = SelectionMenu([])
    list_of_all_clients_submenu_item.append_item(list_of_all_clients_function)
    list_of_all_clients_submenu_item.append_item(find_customer_function)
    list_of_all_clients_submenu_item.append_item(update_client_info_function)
    list_of_all_clients_submenu_item.append_item(remove_client_function)
    list_of_all_clients_submenu_item.append_item(add_new_client_function)

    work_with_accounts_selection_menu = SelectionMenu([])
    work_with_accounts_selection_menu.append_item(get_balance_function)
    work_with_accounts_selection_menu.append_item(open_new_account_function)
    work_with_accounts_selection_menu.append_item(close_account_function)

    process_transactions_selection_menu = SelectionMenu([])
    process_transactions_selection_menu.append_item(add_new_transaction_function)
    process_transactions_selection_menu.append_item(view_transaction_history_function)

    manage_clients_submenu_item = SubmenuItem("Manage clients", list_of_all_clients_submenu_item, menu)

    accounts_submenu_item = SubmenuItem("Work with accounts", work_with_accounts_selection_menu, menu)
    process_transactions_submenu_item = SubmenuItem("Process Transactions", process_transactions_selection_menu, menu)

    menu.append_item(manage_clients_submenu_item)
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
