# How to use multiprocessing.Queue as a FIFO queue

from multiprocessing import Queue


queue = Queue(maxsize=3)
queue.put(1)
print(queue.get())
