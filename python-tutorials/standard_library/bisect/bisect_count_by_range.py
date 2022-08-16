from bisect import bisect_left, bisect_right


# 값이 [left _value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(iterable, left_value, right_value):
    right_index = bisect_right(iterable, right_value)
    left_index = bisect_left(iterable, left_value)
    return right_index - left_index


# 리스트 선언
a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]

# 값이 4인 데이터 개수 출력
print(count_by_range(a, 4, 4))

# 값이 [-1, 3] 범위에 있는 데이터 개수 출력
print(count_by_range(a, -1, 3))
