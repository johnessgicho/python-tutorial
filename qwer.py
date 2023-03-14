import threading

Count = 0
lock = threading.Lock()

def increment_Count(thread_name):
    global Count
    for i in range(5):
        lock.acquire()
        print(f"{thread_name} acquired lock")
        Count += 1
        print(f"{thread_name} incremented Count to {Count}")
        lock.release()
        print(f"{thread_name} released lock")

T1 = threading.Thread(target=increment_Count, args=("Thread 1",))
T2 = threading.Thread(target=increment_Count, args=("Thread 2",))

T1.start()
T2.start()

T1.join()
T2.join()

print("Final Count:", Count)


