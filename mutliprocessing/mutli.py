from multiprocessing import Pool
import time

MX = 30000000

def countdown(count):
    while count:
        count = count - 1

if __name__ == '__main__':
    pool = Pool(processes=2)
    start = time.time()
    r1 = pool.apply_async(countdown, [MX//2])
    r2 = pool.apply_async(countdown, [MX//2])
    pool.close()
    pool.join()
    end = time.time()
    print('Time taken: ', end - start)