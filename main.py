from consolemenu import ConsoleMenu, SelectionMenu
from consolemenu.items import FunctionItem, SubmenuItem

from src import bank as bank, models


def main():
    # Create the menu
    menu = ConsoleMenu("Lena's Bank main menu", "Welcome to Lena's Bank! Please select from the following menu:")

    # A FunctionItem runs a Python function when selected
    list_of_all_customers_function = FunctionItem("List of all customers", bank.list_of_all_customers)
    find_customer_function = FunctionItem("Find customer by SSN", bank.find_customer)
    update_customer_info_function = FunctionItem("Update customer info", bank.update_customer)
    remove_customer_function = FunctionItem("Remove customer", bank.remove_customer)
    add_new_customer_function = FunctionItem("Add new customer", bank.add_new_customer)

    get_balance_function = FunctionItem("Get balance", bank.get_balance)
    open_new_account_function = FunctionItem("Open New Account", bank.open_new_account)
    close_account_function = FunctionItem("Close account", bank.close_account)

    add_new_transaction_function = FunctionItem("Add new transaction", bank.add_new_transaction)
    view_transaction_history_function = FunctionItem("View transaction history", bank.transaction_history)

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


if __name__ == "__main__":
    main()
