# 리스트 컴프리헨션
# 리스트 컴프리헨션은 리스트를 만드는 간결한 방법을 제공합니다.
# 흔한 용도는, 각 요소가 다른 시퀀스나 이터러블의 멤버들에 어떤 연산을 적용한 결과인 리스트를 만들거나, 어떤 조건을 만족하는 요소들로 구성된 서브 시퀀스를 만드는 것입니다.

# 제곱수의 리스트 만들기(loop)
from math import pi

squares = []
for x in range(10):
    squares.append(x ** 2)

print(squares)
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# 제곱수의 리스트 만들기(comprehensions)
squares = list(map(lambda x: x ** 2, range(10)))

print(squares)
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# 두 리스트의 요소들을 서로 같지 않은 것끼리 결합 하기(comprehensions)
# 표현식이 튜플이면 (즉 (x, y)), 반드시 괄호로 둘러싸야 한다.
combs = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]

print(combs)
# [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

# 두 리스트의 요소들을 서로 같지 않은 것끼리 결합 하기(loop)
combs = []
for x in [1, 2, 3]:
    for y in [3, 1, 4]:
        if x != y:
            combs.append((x, y))
print(combs)
# [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

vec = [-4, -2, 0, 2, 4]
# 값이 두 배로 된 새 목록을 만들기.
print([x * 2 for x in vec])
# [-8, -4, 0, 4, 8]

# 음수를 제외 하도록 목록을 필터링
print([x for x in vec if x >= 0])
# [0, 2, 4]

# 모든 요소에 함수 적용
print([abs(x) for x in vec])
# [4, 2, 0, 2, 4]

# 각 요소에 대한 메소드 호출
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
print([weapon.strip() for weapon in freshfruit])
# ['banana', 'loganberry', 'passion fruit']

# (number, square) 2-튜플 목록을 만들기.
print([(x, x ** 2) for x in range(6)])
# [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]

# 튜플은 반드시 괄호로 묶어야 합니다. 그렇지 않으면 오류가 발생합니다.
# print([x, x ** 2 for x in range(6)])
# SyntaxError: invalid syntax

# 두 개의 'for'가 있는 list comprehensions을 사용하여 목록을 병합.
vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print([num for elem in vec for num in elem])
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

print([str(round(pi, i)) for i in range(1, 6)])
# ['3.1', '3.14', '3.142', '3.1416', '3.14159']

# 중첩된 리스트 컴프리헨션
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

# 행과 열을 전치
print([[row[i] for row in matrix] for i in range(4)])
# [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

# 중첩된 리스트 컴프리헨션은 뒤따르는 for 의 문맥에서 값이 구해진다. 이 예는 다음과 동등하다
transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
print(transposed)
# [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

# 내장 함수 zip() 사용
print(list(zip(*matrix)))
# [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]