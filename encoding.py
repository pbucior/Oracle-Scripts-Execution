import codecs
import os
import config as cfg
from charset_normalizer import detect


def check_encoding(file_bytes):
    result = detect(file_bytes)
    encoding = result['encoding']
    return encoding


def encode_file(filename):
    source_filename = os.path.join(cfg.source_dir, filename).replace("\\", "/")
    target_filename = os.path.join(cfg.encoded_dir, filename).replace("\\", "/")
    f = open(source_filename, 'rb')
    source_bytes = f.read()
    source_encoding = check_encoding(source_bytes)
    with codecs.open(source_filename, "r", source_encoding) as sourceFile:
        with codecs.open(target_filename, "w", 'utf-8') as targetFile:
            while True:
                contents = sourceFile.read()
                if not contents:
                    break
                targetFile.write(contents)

