from collections import deque

queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
queue.append("Graham")

print(queue.popleft())
# Eric

print(queue.popleft())
# John

print(queue)
# deque(['Michael', 'Terry', 'Graham'])
