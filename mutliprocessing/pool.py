# Data based parallelism

# Notes from: https://lih-verma.medium.com/multi-processing-in-python-process-vs-pool-5caf0f67eb2b
# For passing in multiple args, try https://stackoverflow.com/questions/5442910/how-to-use-multiprocessing-pool-map-with-multiple-arguments
# map async v map: https://stackoverflow.com/questions/35908987/multiprocessing-map-vs-map-async

from multiprocessing import Pool
from itertools import product

def raise_x_to_3(x):
    print(pow(x,3))

if __name__ == '__main__':
    test = [0, 5, 10, 15, 90, 100, 150]
    with Pool(5) as p:
        # mapping jobs to processes
        pp = p.map_async(raise_x_to_3, test) # map blocks
        pp.wait()

        p.map(raise_x_to_3, test)
