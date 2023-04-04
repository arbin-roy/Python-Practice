from collections import deque

queue = deque(maxlen=4)
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
print(queue)
print(queue.popleft())
print(queue.clear())
print(queue)
