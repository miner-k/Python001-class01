

from multiprocessing import Process

'''
Process(group=None, target=None, name=None, args=(), kwargs={},
                 *, daemon=None)
                 
        group: 分组，实际上很少用
        target： 表示调用对象，你可以传入方法的名字
        name: 别名，相当于给进程起一个别名
        args： 表示被调用对象的位置参数元组，比如target函数的a，他有两个参数m/n,那么args需要传入（m,n）
        kwargs: 表示调用对象的字典

'''
def f(name):
    print(f'hello {name}')  # f str 在python3.6 之后才能使用

if __name__ == '__main__':
    P = Process(target=f,args=('john',))
    P.start()
    P.join()
    P.close()
    P.terminate()

'''
join([timeout])
如果可选参数timeout是None（默认值），则该方法阻塞
直到调用join（）的方法的进程终止，
如果timeout是一个正数，他最多会等待timeout秒

注意：如果进程终止或者超时，则该方法放回None

检查进程的exitcode以确保他是否退出
一个进程可以合并多次
进程无法并入自身，因为这会导致死锁
尝试在启动前合并进程是错误的

'''
