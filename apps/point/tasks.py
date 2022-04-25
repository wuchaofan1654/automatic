# -*- coding:utf-8 -*-
import difflib

from watchdog.observers import Observer
from watchdog.events import *
import time


class FileEventHandler(FileSystemEventHandler):
    def __init__(self):
        FileSystemEventHandler.__init__(self)
        self.fileNameList = []

    def on_moved(self, event):
        if event.is_directory:
            print("directory moved from {0} to {1}".format(event.src_path, event.dest_path))
        else:
            print("file moved from {0} to {1}".format(event.src_path, event.dest_path))

    def on_created(self, event):
        if event.is_directory:
            print("directory created:{0}".format(event.src_path))
        else:
            print("file created:{0}".format(event.src_path))
            fileAllName = str(event.src_path.split('/')[-1])
            if fileAllName.endswith('.py'):
                self.fileNameList.append(fileAllName)
            print(self.fileNameList)

    # 删除文件或文件夹
    def on_deleted(self, event):
        if event.is_directory:
            print("directory deleted:{0}".format(event.src_path))
        else:
            print("file deleted:{0}".format(event.src_path))

    # 修改文件或文件夹
    def on_modified(self, event):
        if event.is_directory:
            print("directory modified:{0}".format(event.src_path))
        else:
            print("file modified:{0}".format(event.src_path))


# if __name__ == "__main__":
    # # 实例化Observer对象
    # observer = Observer()
    # event_handler = FileEventHandler()
    # # 设置监听目录
    # dis_dir = "./"
    # observer.schedule(event_handler, dis_dir, True)
    # observer.start()
    # try:
    #     while True:
    #         # 设置监听频率(间隔周期时间)
    #         time.sleep(1)
    # except KeyboardInterrupt:
    #     observer.stop()
    # observer.join()


# -*- coding: utf-8 -*-
"""
Create by sandy at 20:32 22/03/2022
Description: ToDo
"""

import subprocess


class ShellUtils(object):
    @classmethod
    def __enter__(cls):
        return cls

    @classmethod
    def realtime_output_cmd_stdout(cls, cmd: str):
        xe = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
        while True:
            rt_data = xe.stdout.readline().decode("utf-8")
            if rt_data != "":
                yield rt_data.strip()
            else:
                break

        return xe.wait()

    @classmethod
    def __exit__(cls, exc_type, exc_val, exc_tb):
        if exc_type or exc_val or exc_tb:
            return -1, (exc_type, exc_val, exc_tb)
        else:
            return 0


if __name__ == '__main__':
    class Colors:
        HEADER = '\033[95m'  # pink
        BLUE = '\033[94m'  # blue
        SUCCESS = '\033[92m'  # green
        WARNING = '\033[93m'  # yellow
        DANGER = '\033[91m'  # red
        BLACK = '\033[0m'  # black
        BOLD = '\033[1m'  # black+bold
        UNDERLINE = '\033[4m'  # black+underline


    print(Colors.WARNING + "秋天的颜色字体?")
    print(Colors.DANGER + '我爱你')
