import os
import sys
import datetime
#3 levels up
if not (os.path.dirname(os.path.dirname(os.path.dirname(__file__))) in sys.path): sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
if not (os.path.dirname(os.path.dirname(__file__)) in sys.path): sys.path.append(os.path.dirname(os.path.dirname(__file__)))
if not (os.path.dirname(__file__) in sys.path): sys.path.append(os.path.dirname(__file__))

thisfolder =os.path.dirname(__file__)
module_id = os.path.basename(thisfolder)
module_version = 0.1

from _serverApp import thisApp
from _serverApp import log_message
from _serverApp import retrieve_module_configuration

from _database_ganimides_engine import engine_session,get_dbsession
# from _database_ganimides import db_model
from _database_ganimides import db_schema
#adminServices
from _database_adminServices import drop_table,check_table,recreate_tables

#models
from _database_ganimides_model import TEST
from _database_ganimides_model import USER
from _database_ganimides_model import DEPARTMENT
from _database_ganimides_model import EMPLOYEE
from _database_ganimides_model import API
from _database_ganimides_model import APPLICATION
from _database_ganimides_model import CLIENT
from _database_ganimides_model import CLIENT_CONFIRMATION
from _database_ganimides_model import SERVICE_PROVIDER
from _database_ganimides_model import APPLICATION_API
from _database_ganimides_model import TOKEN
from _database_ganimides_model import DEVICE
from _database_ganimides_model import DEVICE_USAGE
from _database_ganimides_model import CLIENT_DEVICE
from _database_ganimides_model import VERIFICATION
from _database_ganimides_model import EMAIL
from _database_ganimides_model import SMS
from _database_ganimides_model import MERCHANT
from _database_ganimides_model import MERCHANT_EMPLOYEE
from _database_ganimides_model import POINT_OF_SALE
from _database_ganimides_model import CONSUMER
from _database_ganimides_model import INTERACTION
from _database_ganimides_model import INTERACTION_MESSAGE
from _database_ganimides_model import BANK
from _database_ganimides_model import BANK_AUTHORIZATION
from _database_ganimides_model import BANK_SUBSCRIPTION
from _database_ganimides_model import BANK_ACCOUNT
from _database_ganimides_model import APPLICATION_USER
from _database_ganimides_model import APPLICATION_TEMPLATE

#tables
from _database_ganimides_schema import TEST_TABLE
from _database_ganimides_schema import USERS_TABLE
from _database_ganimides_schema import DEPARTMENTS_TABLE
from _database_ganimides_schema import EMPLOYEES_TABLE
from _database_ganimides_schema import APIS_TABLE
from _database_ganimides_schema import APPLICATIONS_TABLE
from _database_ganimides_schema import CLIENTS_TABLE
#from _database_ganimides_schema import SERVICE_PROVIDERS_TABLE
from _database_ganimides_schema import REGISTERED_APIS_TABLE
from _database_ganimides_schema import TOKENS_TABLE
from _database_ganimides_schema import DEVICES_TABLE
from _database_ganimides_schema import DEVICE_USAGE_TABLE
from _database_ganimides_schema import CLIENT_DEVICES_TABLE
from _database_ganimides_schema import MERCHANTS_TABLE
from _database_ganimides_schema import MERCHANT_EMPLOYEES_TABLE
from _database_ganimides_schema import POINTS_OF_SALE_TABLE
from _database_ganimides_schema import CONSUMERS_TABLE
from _database_ganimides_schema import INTERACTIONS_TABLE
from _database_ganimides_schema import INTERACTIONS_MESSAGE_TABLE
from _database_ganimides_schema import BANKS_TABLE
from _database_ganimides_schema import BANK_AUTHORIZATIONS_TABLE
from _database_ganimides_schema import BANK_SUBSCRIPTIONS_TABLE
from _database_ganimides_schema import BANK_ACCOUNTS_TABLE

#dbapis
import _database_ganimides_api as dbapi
from _database_ganimides_api import dbapi_api
from _database_ganimides_api import dbapi_api_register_unregister
from _database_ganimides_api import dbapi_application
from _database_ganimides_api import dbapi_application_USER
from _database_ganimides_api import dbapi_application_template
from _database_ganimides_api import dbapi_application_api
from _database_ganimides_api import dbapi_application_credentials_are_valid
from _database_ganimides_api import dbapi_bank
from _database_ganimides_api import dbapi_bank_account
from _database_ganimides_api import dbapi_bank_authorization
from _database_ganimides_api import dbapi_bank_subscription
from _database_ganimides_api import dbapi_cleanup_tokens
from _database_ganimides_api import dbapi_client
from _database_ganimides_api import dbapi_client_device
from _database_ganimides_api import dbapi_email_confirmation
from _database_ganimides_api import dbapi_mobile_confirmation
from _database_ganimides_api import dbapi_verification
from _database_ganimides_api import dbapi_customer_service_assistant
from _database_ganimides_api import dbapi_device
from _database_ganimides_api import dbapi_device_log
from _database_ganimides_api import dbapi_device_register_unregister
from _database_ganimides_api import dbapi_device_usage
from _database_ganimides_api import dbapi_get_bank_account_id
from _database_ganimides_api import dbapi_get_bank_code
from _database_ganimides_api import dbapi_interaction
from _database_ganimides_api import dbapi_interaction_accept
from _database_ganimides_api import dbapi_interaction_finish
from _database_ganimides_api import dbapi_interaction_message
from _database_ganimides_api import dbapi_interaction_message_add
from _database_ganimides_api import dbapi_interaction_start
from _database_ganimides_api import dbapi_merchant
from _database_ganimides_api import dbapi_merchant_bankaccount_register
from _database_ganimides_api import dbapi_merchant_get_bankaccounts
from _database_ganimides_api import dbapi_pointofsale
from _database_ganimides_api import dbapi_pointofsale_bankaccount_add
from _database_ganimides_api import dbapi_pointofsale_bankaccount_remove
from _database_ganimides_api import dbapi_pointofsale_credit_info
from _database_ganimides_api import dbapi_retail_store
from _database_ganimides_api import dbapi_service_point
from _database_ganimides_api import dbapi_subscription
from _database_ganimides_api import dbapi_token
from _database_ganimides_api import dbapi_token_get_access_token
from _database_ganimides_api import dbapi_token_is_valid
from _database_ganimides_api import dbapi_user
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#::: module                                                                                                 :::
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
thisfolder =os.path.dirname(__file__)
module_id = 'ganimides_database'
module_version = 0.1

module_Function = 'database server'
module_ProgramName = 'ganimides_database'
module_BaseTimeStamp = datetime.datetime.now()
module_folder = os.getcwd()
module_color = thisApp.Fore.LIGHTMAGENTA_EX
module_folder = os.path.dirname(__file__)
module_ProgramName = os.path.splitext(os.path.basename(__file__))[0]
#module_id = f'{module_ProgramName}'
module_eyecatch = module_id
#module_version = 0.1
module_log_file_name = module_id+'.log'
module_errors_file_name = os.path.splitext(os.path.basename(module_log_file_name))[0]+'_errors.log'
module_versionString = f'{module_id} version {module_version}'
module_file = module_id

# log_file=thisApp.log_file_name
# print_enabled = thisApp.CONSOLE_ON
# consolelog_enabled = thisApp.CONSOLE_ON
# filelog_enabled = thisApp.FILELOG_ON

module_is_externally_configurable = False
module_identityDictionary = {
    'module_file':module_id,
    'module_Function':module_Function,
    'module_ProgramName':module_ProgramName,
    'module_BaseTimeStamp':module_BaseTimeStamp,
    'module_folder':module_folder,
    'module_color':module_color,
    'module_id':module_id,
    'module_eyecatch':module_eyecatch,
    'module_version':module_version,
    'module_versionString':module_versionString,
    'module_log_file_name':module_log_file_name,
    'module_errors_file_name': module_errors_file_name,
    # 'consolelog_enabled': consolelog_enabled,
    # 'filelog_enabled': filelog_enabled,
    'module_is_externally_configurable':module_is_externally_configurable,
    }
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# configuration
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
module_configuration = {
    "application_id": module_id,
    "application_name": 'ganimidesServer',
    "application_title": 'ganimides server',
    "application_version": module_version,
    "application_function": module_Function,
    "application_ProgramName": module_ProgramName,
    "application_folder": module_folder,
    }
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# module initialization
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
module_configuration = retrieve_module_configuration(__file__, module_identityDictionary, module_configuration, print_enabled=thisApp.DEBUG_ON, filelog_enabled=thisApp.FILELOG_ON, handle_as_init=False)
thisApp.pair_application_configuration(module_configuration, module_identityDictionary)
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
msg = f'PACKAGE module [{module_id}] [[version {module_version}]] loaded.'
if thisApp.get_module_debug_level(module_id):
    log_message(msg)
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
