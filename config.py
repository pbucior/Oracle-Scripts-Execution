import getpass
import os
import configparser
import oracledb
from datetime import datetime

p_password = getpass.getpass("Hasło do bazy danych: ")


try:
    config = configparser.ConfigParser()
    config.read('config.ini')
    database = config['Database']
    p_username = database['Schema']
    p_host = database['Host']
    p_service = database['Service']
    p_port = database['Port']
    connection_string = p_username + '/' + p_password + '@' + p_host + ':' + p_port + '/' + p_service
    dsn_str = oracledb.makedsn(p_host, p_port, p_service)
    errors = config['Errors']
    ok_errors = errors['Excluded']
except:
   print("Brak pliku config.ini")

# Ściezka do katalogu z plikami SQL
root_dir_name = os.getcwd()
source_dir = os.path.join(root_dir_name, 'sql_source')
encoded_dir = os.path.join(root_dir_name, 'sql_encoded')
executed_dir = os.path.join(root_dir_name, 'sql_executed')
log_dir = os.path.join(root_dir_name, 'log')
log_filename = datetime.now().strftime('%Y-%m-%d_%H-%M-%S') + '.log'
log_file = os.path.join(log_dir, log_filename)

