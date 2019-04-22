import threading
import time

def run(lock):
    global channel
    print("Before Locked State: {}".format(threading.current_thread().name))
    lock.acquire()
    time.sleep(1)
    print("Locked State: {}".format(threading.current_thread().name))
    if channel == 0:
        channel = 1
        print("Channel set to  1 by: {}".format(threading.current_thread().name))
        time.sleep(1)
    else:
        while channel:
            time.sleep(1)
            print("Loop State: {}".format(threading.current_thread().name))
        else:
            channel = 1
            print("Channel set to  1 by: {}".format(threading.current_thread().name))
            time.sleep(1)
    lock.release()
    time.sleep(5)
    channel = 0


channel = 0
lock = threading.Lock()
for i in range(2):
    t1 = threading.Thread(target = run, name = str(i), args=(lock,))
    t1.start()
else:
    t1.join()
    print("Finished")
