import queue as q

cQ = q.Queue(maxsize=4)
print(cQ.qsize())
cQ.put(1)
cQ.put(2)
cQ.put(3)
cQ.put(4)
print(cQ.get())

