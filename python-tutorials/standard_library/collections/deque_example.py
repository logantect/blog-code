from collections import deque

data = deque([2, 3, 4])
data.appendleft(1)
data.append(5)
print(data)
print(list(data)) # 리스트 자료형으로 변환
