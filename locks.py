import threading

total = 0
lock = threading.Lock()

def update_total(amt):
    global total
    with lock:
        total += amt
    print(total)


for i in  range(10):
    my_threads = threading.Thread(target=update_total, args=(5,))
    my_threads.start()