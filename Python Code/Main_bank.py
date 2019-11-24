# print welcome message
print("Welcome to Lena's Bank!\n" + "Please select from the following menu.")

# Displaying the main menu
main_menu_dict = {1: "Manage Clients", 2: "Work with accounts", 3: "Process Transactions"}

for key, value in main_menu_dict.items():
    print("Type ", key, "to ", value)


# input function for main menu
def main_menu_options():
    x = int(input("Enter a number 1-3: "))
    if x == 1:
        print("printManageClientsMenu()")
    elif x == 2:
        print("printWorkWithAccountsMenu()")
    elif x == 3:
        print("printProcessTransactionsMenu()")
    else:
        print("This is an incorrect entry. Please enter a number between 1 and 3")


main_menu_options()

# if you choose 1 then calls printManageClientsMenu and so on

# def printManageClientsMenu():
# print("bla bla ")
