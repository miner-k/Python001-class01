
import os
import time
from multiprocessing import Process

def run():
    print('子进程开始')
    time.sleep(3)
    print('子进程结束')

if __name__ == '__main__':
    print('父进程开始')
    p = Process(target=run)
    p.start()
    p.join()
    print('父进程结束')