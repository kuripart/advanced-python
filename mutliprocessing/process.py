# Function based parallelism
from multiprocessing import Process

def foo(test):
    print('testing: ', test)

def bar(test):
    print('testing: ', test)

if __name__ == '__main__':
    p1 = Process(target=foo, args=('foo',))
    p1.start() # asynchronously start preocess
    p2 = Process(target=bar, args=('bar',))
    p2.start()
    # NOTE: can only join a started process
    p1.join()
    p2.join()