import re
import config as cfg


def get_error_codes(message):
    indices_object = re.finditer(pattern='ORA-', string=message)
    indices = [index.start() for index in indices_object]
    errors = []
    all_errors = []
    for idx in indices:
        error = message[idx:idx+9]
        if error not in cfg.ok_errors:
            errors.append(error)
        all_errors.append(error)
    return errors, all_errors


def log_to_file(text):
    file = open(cfg.log_file, "a")
    file.write(text + '\n')
    file.close()


