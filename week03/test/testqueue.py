

from multiprocessing import Process, Queue

def f(q):
    q.put([42, None, 'hello'])  # 队列的写操作，写入一个列表

if __name__ == '__main__':
    q = Queue()  # 默认不指定队列的长度，就是内存的大小，实际使用，建议定义队列的长度
    p = Process(target=f, args=(q,))
    p.start()
    print(q.get())    #获取队列中的内容 prints "[42, None, 'hello']"
    p.join()

# 队列是线程和进程安全的