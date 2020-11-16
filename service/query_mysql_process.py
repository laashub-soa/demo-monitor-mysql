from component import mymysql

def query():
    print(mymysql.execute("select count(1) from information_schema.processlist"))
