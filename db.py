import os
from subprocess import Popen, PIPE
import oracledb
import config as cfg


def run_sqlplus(sql, connect_string):
    my_env = os.environ.copy()
    my_env['NLS_LANG'] = 'POLISH_POLAND.AL32UTF8'
    session = Popen(['sqlplus', '-S', connect_string], stdin=PIPE, stdout=PIPE, stderr=PIPE, env=my_env)
    session.stdin.write(sql)
    return session.communicate()


def check_sql_history(file):
    con = oracledb.connect(user=cfg.p_username, password=cfg.p_password, dsn=cfg.dsn_str)
    cur = con.cursor()
    query = 'select * from script_logs where upper(script_name) = \'' + file.upper() + '\''
    cur.execute(query)
    result = cur.fetchall()
    is_exists = len(result)
    cur.close()
    con.close()
    return is_exists

