import multiprocessing


def worker (num):
    print(f" worker{num} is running with process ID {multiprocessing.current_process().pid}")
if __name__ == "__main__":
    P1 = multiprocessing.Process(target=worker,args=(1,))
    P2 = multiprocessing.Process(target=worker,args=(2,))
    P1.start()
    P2.start()
