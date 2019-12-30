from unittest.mock import patch, Mock
import io

import sys
from tabulate import tabulate
from unittest import TestCase

sys.modules['models'] = Mock()
from src.models import Customer, Account
import src.main_bank as mb



def get_customer():
    customer = Customer()
    customer.Id = 123
    customer.name = 'Klaudius'
    customer.address = 'Ave Street'
    customer.dob = '1985-01-01'
    customer.ssn = 1234567890
    customer.phone_number = 1890765432
    customer.email = 'mail@mail.ua'
    return customer


class Test(TestCase):

    @patch('main_bank.models.list_of_bank_customers')
    def test_list_of_all_customers(self, mock_models):
        mb.list_of_all_customers()
        self.assertTrue(mock_models.called)

    @patch('builtins.input', return_value=1234567890)
    @patch('main_bank.models.find_customer')
    def test_find_customer_not_found(self, mock_models_find, input):
        mock_models_find.return_value = None
        mb.find_customer()
        mock_models_find.assert_called_with(1234567890)

    @patch('builtins.input', return_value=1234567890)
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('main_bank.models.find_customer')
    def test_find_customer(self, mock_models_find, mock_stdout, mock_input):
        customer = get_customer()
        mock_models_find.return_value = customer
        mb.find_customer()
        self.assertEqual(mock_stdout.getvalue(), "\nInfo for customer " + customer.name + " is below: \n" + tabulate(
            [["Customer's Id ", customer.Id], ["Customer's name ", customer.name],
             ["Customer's Address ", customer.address], ["Customer's Date of Birth ", customer.dob],
             ["Customer's SSN ", customer.ssn], ["Customer's phone Number ", customer.phone_number],
             ["Customer's email ", customer.email]], tablefmt="fancy_grid") + "\n")

    @patch('builtins.input', return_value=1234567890)
    @patch('main_bank.models.find_customer')
    def test_update_customer_not_found(self, mock_models_find, input):
        mock_models_find.return_value = None
        mb.update_customer()
        mock_models_find.assert_called_with(1234567890)

    @patch('builtins.input',
           side_effect=[1234567890, 'Klaudius1', 'Ave Street 1', '1985-01-01', 1234567890, '1876543210', 'mail@mail.ua',
                        1234567890, 'Savings'])
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('main_bank.models.update_customer_info')
    @patch('main_bank.models.find_customer')
    def test_update_customer_found(self, mock_models_find, mock_models_update, mock_stdout, input):
        customer = get_customer()
        mock_models_find.return_value = customer
        mb.update_customer()
        mock_models_find.assert_called_with(1234567890)
        mock_models_find.update_customer_info(customer)
        self.assertEqual(mock_stdout.getvalue(),
                         "Existing Customer Current Name: Klaudius\n\nCustomer's profile has been updated\n",
                         msg='Not Equal')
        self.assertEqual(customer.name, 'Klaudius1')
        self.assertEqual(customer.address, 'Ave Street 1')

    @patch('builtins.input', return_value=1234567890)
    @patch('main_bank.models.find_customer')
    def test_remove_customer_not_found(self, mock_models_find, input):
        mock_models_find.return_value = None
        mb.remove_customer()
        mock_models_find.assert_called_with(1234567890)

    @patch('builtins.input', return_value=1234567890)
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('main_bank.models.find_customer')
    @patch('main_bank.models.delete_customer')
    def test_remove_customer_found(self, models_mock_delete, models_mock_find, mock_stdout, mock_input):
        customer = get_customer()
        models_mock_find.return_value = customer
        models_mock_delete.return_value = customer

        mb.remove_customer()

        models_mock_find.assert_called_with(1234567890)
        models_mock_delete.assert_called_with(customer)
        self.assertEqual(mock_stdout.getvalue(), "Customer Klaudius is deleted\n", msg='Not Equal')

    @patch('builtins.input',
           side_effect=['Klaudius', 'Ave Street', '1985-01-01', 1234567890, '1876543210', 'mail@mail.ua', 1234567890,
                        'Savings'])
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('main_bank.models.insert_customer')
    def test_add_new_customer(self, mock_models, mock_stdout, mock_input):
        mb.add_new_customer()
        self.assertEqual(mock_stdout.getvalue(),
                         "\nNew customer Klaudius has been added. Please verify the following info: \n" + tabulate(
                             [["Name ", 'Klaudius'], ["Address ", 'Ave Street'], ["Date of Birth ", '1985-01-01'],
                              ["SSN ", 1234567890], ["Phone Number ", 1876543210],
                              ["Email ", 'mail@mail.ua'], ["Account number ", 1234567890], ["Type ", 'Savings']],
                             tablefmt="fancy_grid") + "\n")

        mock_models.assert_called_with(name_param='Klaudius', address_param='Ave Street',
                                       dob_param='1985-01-01', ssn_param=1234567890, phone_number_param='1876543210',
                                       email_param='mail@mail.ua', account_no_param=1234567890,
                                       account_type_param='Savings')

    @patch('builtins.input', return_value=1234567890)
    @patch('main_bank.models.check_balance')
    def test_check_balance_not_found(self, mock_models_balance, input):
        mock_models_balance.return_value = None
        mb.get_balance()
        mock_models_balance.assert_called_with(1234567890)

    @patch('builtins.input', return_value=1234567890)
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('main_bank.models.check_balance')
    def test_check_balance_found(self, models_mock_check, mock_stdout, mock_input):
        models_mock_check.return_value = 123
        mb.get_balance()
        self.assertEqual(mock_stdout.getvalue(), "\nAccount balance: $123\n", msg='Not Equal')

    @patch('builtins.input', return_value=1234567890)
    @patch('main_bank.models.find_customer')
    def test_open_new_account_customer_not_found(self, mock_models_find, input):
        mock_models_find.return_value = None
        mb.open_new_account()
        mock_models_find.assert_called_with(1234567890)

    @patch('builtins.input', side_effect=[1234567890, 1876543210, 'bla'])
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('main_bank.models.find_customer')
    def test_open_new_account_customer_found(self, models_mock_find, mock_stdout, mock_input):
        customer = get_customer()
        models_mock_find.return_value = customer

        mb.open_new_account()

        models_mock_find.assert_called_with(1234567890)
        self.assertEqual(mock_stdout.getvalue(), "Invalid entry. Please enter valid account type\n", msg='Not Equal')

    @patch('builtins.input', side_effect=[1234567890, 1876543210, 'Savings'])
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('main_bank.models.find_customer')
    @patch('main_bank.models.open_new_account')
    def test_open_new_account_customer_found_and_correct_type(self, models_mock_open, models_mock_find, mock_stdout,
                                                              mock_input):
        customer = get_customer()
        models_mock_find.return_value = customer

        mb.open_new_account()

        models_mock_find.assert_called_with(1234567890)
        models_mock_open.assert_called_with(customer, account_no_param=1876543210, account_type_param='Savings')
        self.assertEqual(mock_stdout.getvalue(),
                         "\nNew account number 1876543210 has been added to customer's profile\n", msg='Not Equal')

    @patch('builtins.input', return_value=1234567890)
    @patch('main_bank.models.close_existing_account')
    def test_close_account(self, mock_models, input):
        mb.close_account()
        mock_models.assert_called_with(account_num_param=1234567890)

    @patch('builtins.input', return_value=1234567890)
    @patch('main_bank.models.get_account')
    def test_add_new_transaction_account_not_found(self, mock_models_get_account, input):
        mock_models_get_account.return_value = None
        mb.add_new_transaction()
        mock_models_get_account.assert_called_with(1234567890)

    @patch('builtins.input', side_effect=[1234567890, 'Deposit', 1234])
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('main_bank.models.get_account')
    @patch('main_bank.models.add_new_transaction')
    def test_add_new_transaction(self, mock_models_new_trans, mock_models_get_account, mock_stdout, input):
        mock_models_get_account.return_value = Account()
        mb.add_new_transaction()
        mock_models_get_account.assert_called_with(1234567890)
        mock_models_new_trans.assert_called_with(account_no_param=1234567890, transaction_type_param='Deposit',
                                                 transaction_amount_param=1234)
        self.assertEqual(mock_stdout.getvalue(),
                         "\nDeposit transaction for $1234 has been added. Please verify transaction details below: \n" + tabulate(
                             [["Account Number ", 1234567890], ["Type ", 'Deposit'], ["Amount ", 1234]],
                             tablefmt="fancy_grid") + "\n", msg='Not Equal')

    @patch('builtins.input', return_value=1234567890)
    @patch('main_bank.models.show_transactions')
    def test_transaction_history(self, mock_models, input):
        mb.transaction_history()
        mock_models.show_transactions(account_no=1234567890)
