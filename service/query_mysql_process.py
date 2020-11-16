#!/usr/local/bin/python
# coding: utf-8
import json
import os
import time
from datetime import datetime

if __name__ == '__main__':
    command_template = """
    mysql -h {host} -P {port} -u {username} -p{password} -e "show processlist;"
    """
    base_dir = "/data/tristan/query_mysql_process"
    if not os.path.exists(base_dir):
        os.system("mkdir -p " + base_dir)
        print("创建基础目录")
    data_data = None
    with open("data_data_query_mysql_process.json")as file:
        file_content = file.read()
        data_data = json.loads(file_content)
    data_data_mysql = data_data["mysql"]
    command = command_template.format(**{
        "host": data_data_mysql["host"],
        "port": data_data_mysql["port"],
        "username": data_data_mysql["username"],
        "password": data_data_mysql["password"],
    })
    while True:
        out_log = os.popen(command).read()
        datetime_now = datetime.now()
        datetime_now_day_list_str = datetime_now.strftime('%Y-%m-%d')
        dir_path = base_dir + "/" + str(datetime_now_day_list_str)
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
            print("创建日期目录")
        datetime_now_day_details_str = datetime_now.strftime('%H-%M-%S')
        with open(dir_path + "/" + datetime_now_day_details_str + ".txt", "w") as file:
            file.write(out_log)
            print("写入上5秒钟查询出来的mysql进程信息")
        time.sleep(5)
