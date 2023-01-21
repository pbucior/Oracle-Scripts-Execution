import os
import shutil
import config as cfg
import utils
import db
import encoding


if not os.path.isdir(cfg.source_dir):
    os.makedirs(cfg.source_dir)
if not os.path.isdir(cfg.encoded_dir):
    os.makedirs(cfg.encoded_dir)
if not os.path.isdir(cfg.executed_dir):
    os.makedirs(cfg.executed_dir)
if not os.path.isdir(cfg.log_dir):
    os.makedirs(cfg.log_dir)


file_list = os.listdir(cfg.source_dir)
file_list.sort()


for file in file_list:
    print(file)
    encoding.encode_file(file)
    source_filepath = os.path.join(cfg.source_dir, file).replace("\\", "/")
    destination_filepath = os.path.join(cfg.executed_dir, file).replace("\\", "/")
    filepath = os.path.join(cfg.encoded_dir, file).replace("\\", "/")
    f = open(filepath, 'rb')
    file_bytes = f.read()
    f.close()
    dest_encoding = encoding.check_encoding(file_bytes)
    utils.log_to_file(file)
    is_sql_history = db.check_sql_history(file)
    if is_sql_history > 0:
        message = 'Skrypt był już wykonywany'
        shutil.move(source_filepath, destination_filepath)
        utils.log_to_file(message)
        print(message)
        continue
    queryResult, errorMessage = db.run_sqlplus(file_bytes, cfg.connection_string)
    message = str(queryResult)
    errors, all_errors = utils.get_error_codes(message)
    is_error = len(errors)
    print(errors)
    print(queryResult.decode())

    if is_error == 0:
        shutil.move(source_filepath, destination_filepath)
        utils.log_to_file('OK')
        utils.log_to_file(str(all_errors))
        utils.log_to_file(queryResult.decode())
        utils.log_to_file('-' * 40)
        continue
    else:
        utils.log_to_file(str(all_errors))
        utils.log_to_file(queryResult.decode())
        utils.log_to_file('-' * 40)
        break


input("Naciśnij ENTER...")