import os
import sys
#3 levels up
if not (os.path.dirname(os.path.dirname(os.path.dirname(__file__))) in sys.path): sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
if not (os.path.dirname(os.path.dirname(__file__)) in sys.path): sys.path.append(os.path.dirname(os.path.dirname(__file__)))
if not (os.path.dirname(__file__) in sys.path): sys.path.append(os.path.dirname(__file__))

thisfolder =os.path.dirname(__file__)
module_id = os.path.basename(thisfolder)
module_version = 0.1

# from _serverApp import thisApp
from _serverApp import thisApp
from _serverApp import log_message

#openbanking apis
from _ganimides_openBankingAPI import bankaccount_remove
from _ganimides_openBankingAPI import banksubscription_create
from _ganimides_openBankingAPI import banksubscription_receive_authorization_from_client
from _ganimides_openBankingAPI import banksubscription_register
from _ganimides_openBankingAPI import banksubscription_request_authorization_from_client
from _ganimides_openBankingAPI import banksubscription_unregister
from _ganimides_openBankingAPI import client_banksubscription_register
from _ganimides_openBankingAPI import merchant_banksubscription_register

from ganimides_bankingAPI import authorize_and_commit_subscription
from ganimides_bankingAPI import authorize_payment
from ganimides_bankingAPI import authorize_subscription
from ganimides_bankingAPI import bank_is_supported
from ganimides_bankingAPI import change_subscription
from ganimides_bankingAPI import commit_subscription
from ganimides_bankingAPI import create_authorize_and_commit_subscription
from ganimides_bankingAPI import create_subscription
from ganimides_bankingAPI import delete_payment
from ganimides_bankingAPI import delete_subscription
from ganimides_bankingAPI import get_access_token
from ganimides_bankingAPI import get_account_balances
from ganimides_bankingAPI import get_account_details
from ganimides_bankingAPI import get_account_payments
from ganimides_bankingAPI import get_account_subscriptions
from ganimides_bankingAPI import get_account_transactions
from ganimides_bankingAPI import get_authorization_token
from ganimides_bankingAPI import get_payment_details
from ganimides_bankingAPI import get_payment_status
from ganimides_bankingAPI import get_subscription_accounts
from ganimides_bankingAPI import get_subscription_customers
from ganimides_bankingAPI import get_subscription_details
from ganimides_bankingAPI import post_payment

msg = f'module [{module_id}] [[version {module_version}]] loaded.'
if thisApp.get_module_debug_level(module_id):
    log_message(msg)
