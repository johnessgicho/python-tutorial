import threading
Count = 0
lock = threading.lock()
def increment_Count(thread_name):
global count
for i in range (5):
    lock.acquire()
    print(f"{thread_name}acquired lock")
    Count +=1
    print(f"{thread_name}incremented Count to {Count}")
    lock.release()
    print(f"{thread_name}released lock")
    t1 = threading.Thread(target= increment_count,args=("Thread 1"))
    t2 = threading.Thread(target= increment_count,args=("Thread 2"))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("fainal count:",Count)