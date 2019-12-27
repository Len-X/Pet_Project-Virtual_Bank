# Import the necessary packages
from consolemenu import *
from consolemenu.items import *
import Models as models
from tabulate import tabulate

def list_of_all_clients():
    models.listofBankClients()

def find_customer():
    SSN = input("Please enter client's SSN: ")
    existingCustomer = models.findCustomer(SSN)
    if existingCustomer == None:
        print("Client Not Found")
    else:
        print("\nInfo for client " + existingCustomer.clientName + " is below: ")
        print(tabulate([["Client's Id ", existingCustomer.id], ["Client's name ", existingCustomer.clientName],
              ["Client's Address ", existingCustomer.clientAddress],["Client's Date of Birth ", existingCustomer.dob],
              ["Client's SSN ", existingCustomer.SSN], ["Client's phone Number ", existingCustomer.phoneNumber],
              ["Client's email ", existingCustomer.email]], tablefmt="fancy_grid"))


def update_client():
    SSN = input("Please enter client's SSN: ")
    founded_customer = models.findCustomer(SSN)
    if founded_customer == None:
        print("Client Not Found")
        return
    print("Existing Customer Current Name: "+founded_customer.clientName)
    newclientName = input("Please enter client's new name, otherwise hit 'Enter': ")
    if newclientName:
        founded_customer.clientName = newclientName
    newClientAddress = input("Please enter client's new address, otherwise hit 'Enter': ")
    if newClientAddress:
        founded_customer.clientAddress = newClientAddress
    newclientsDOB = input("Please enter client's new Date of Birth (YYYY-MM-DD), otherwise hit 'Enter': ")
    if newclientsDOB:
        founded_customer.dob = newclientsDOB
    newclientsSSN = input("Please enter client's new SSN, otherwise hit 'Enter': ")
    if newclientsSSN:
        founded_customer.SSN = newclientsSSN
    newclientsPhoneNo = input("Please enter client's new phone number, otherwise hit 'Enter': ")
    if newclientsPhoneNo:
        founded_customer.phoneNumber = newclientsPhoneNo
    newclientsEmail = input("Please enter client's new email, otherwise hit 'Enter': ")
    if newclientsEmail:
        founded_customer.email = newclientsEmail



    models.updateCustomerInfo(founded_customer)

def remove_client():
    SSN = input("Please enter client's SSN: ")
    existingCustomer = models.findCustomer(SSN)
    if existingCustomer == None:
        print("Client Not Found")
        return
    models.deleteCustomer(existingCustomer.SSN)
    print("Client " +existingCustomer.clientName + " is deleted")


def add_new_client():
    newclientName = str(input("Please enter client's name (First name Last name), then hit 'Enter': "))
    newClientAddress = str(input("Please enter client's address, then hit 'Enter': "))
    newclientsDOB = input("Please enter client's Date of Birth (YYYY-MM-DD), then hit 'Enter': ")
    newclientsSSN = input("Please enter client's SSN, then hit 'Enter': ")
    newclientsPhoneNo = input("Please enter client's phone number, then hit 'Enter': ")
    newclientsEmail = str(input("Please enter client's email, then hit 'Enter': "))
    newAccountNo = input("Please enter client's 10-digit account number, then hit 'Enter': ")
    models.insertCustomer(clientNameParam = newclientName, clientAddressParam = newClientAddress,
                          dobParam = newclientsDOB, SSNParam = newclientsSSN, phoneNumberParam = newclientsPhoneNo,
                          emailParam = newclientsEmail,accountNoParam = newAccountNo)
    print("\nNew client " +newclientName + " has been added. Please verify the following info: ")
    print(tabulate([["Name ", newclientName], ["Address ", newClientAddress], ["Date of Birth ", newclientsDOB],
                    ["SSN ", newclientsSSN], ["Phone Number ", newclientsPhoneNo],
                    ["Email ", newclientsEmail], ["Account number ", newAccountNo]], tablefmt="fancy_grid"))


def get_balance():
    accountNo = input("Please enter client's 10-digit account number, then hit 'Enter': ")
    existing_acct_balance = models.checkBalance(accountNo)
    if existing_acct_balance != None:
        print("\nAccount balance: $" + str(existing_acct_balance))


def open_new_account():
    SSN = input("Please enter client's SSN: ")
    existingCustomer = models.findCustomer(SSN)
    if existingCustomer == None:
        print("Client Not Found")
        return
    newAccountNo = input("Please enter new 10-digit account number, then hit 'Enter': ")
    models.openNewAccount(SSN=SSN, accountNoParam = newAccountNo)
    print("\nNew account number " + newAccountNo + " has been added to client's profile")


def close_account():
    accountNo = input("Please enter client's 10-digit account number that you wish to delete, then hit 'Enter': ")
    models.closeExistingAccount(accountNumParam = accountNo)

def add_new_transaction():
    accountNo = input("Please enter client's 10-digit account number, then hit 'Enter': ")
    transaction_type = str(input("Please enter type of transaction (Deposit, Withdrawal, Interest, Payment): "))
    transaction_amount = input("Please enter transaction amount ('+' or '-'): ")
    models.addNewTransaction(accountNo=accountNo, transactionTypeParam=transaction_type,
                             transactionAmountParam=transaction_amount)
    print("\n"+transaction_type + " transaction for $" + transaction_amount +
          " has been added. Please verify transaction details below: ")
    print(tabulate([["Account Number ", accountNo], ["Type ", transaction_type], ["Amount ", transaction_amount]],
                   tablefmt="fancy_grid"))


def transaction_history():
    accountNo = input("Please enter client's 10-digit account number, then hit 'Enter': ")
    models.ShowTransactions(accountNo=accountNo)




def main():
    # Create the menu
    menu = ConsoleMenu("Lena's Bank main menu", "Welcome to Lena's Bank! Please select from the following menu:")
    # Create some items

    # MenuItem is the base class for all items, it doesn't do anything when selected
    menu_item = MenuItem("Menu Item")

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


    # Once we're done creating them, we just add the items to the menu

    menu.append_item(manage_clients_submenu_item)
    menu.append_item(accounts_submenu_item)
    menu.append_item(process_transactions_submenu_item)

    # Finally, we call show to show the menu and allow the user to interact
    menu.show()

if __name__ == "__main__":
    main()