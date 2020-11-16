from __init__ import do_init
from service import query_mysql_process

do_init()
if __name__ == '__main__':
    query_mysql_process.query()
