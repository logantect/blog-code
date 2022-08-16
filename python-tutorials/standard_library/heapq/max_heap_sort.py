import heapq


# 힙에 원소를 삽입하기 전 에 잠시 부호를 반대로 비꾸었다가, 힙에서 원소를 꺼낸 뒤에 다시 원소의 부호를 바꾼다
def max_heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, -value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for _ in range(len(h)):
        result.append(-heapq.heappop(h))
    return result


result = max_heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)
