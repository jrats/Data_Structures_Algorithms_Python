from collections import deque 

queue = deque(maxlen = 3)
print(queue)

queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
print(queue)
print(queue.popleft())
print(queue)
queue.clear()
print(queue)

####################################

import queue as q

my_q = q.Queue(maxsize=3)
print(my_q.qsize())
print(my_q.empty())
my_q.put(1)
my_q.put(2)
my_q.put(3)
my_q.put(4)
print(my_q)
print(my_q.full())
print(my_q.get())
print(my_q.qsize())

####################################

from multiprocessing import Queue

q = Queue(maxsize=3)

q.put(1)
q.put(14)
q.put(23)
print(q.get())
print(q.get())    #other methods similar to the queue module used above

#################################################