import config
from component import mymysql

config.init()
print(str(config.app_conf))
mymysql.init(config.app_conf["mysql"])


def do_init():
    pass