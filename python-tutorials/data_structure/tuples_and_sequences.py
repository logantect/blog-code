# 튜플과 시퀀스
# 튜플은 쉼표로 구분되는 여러 값으로 구성됩니다.
t = 12345, 54321, 'hello!'
print(t[0])
# 12345

print(t)
# (12345, 54321, 'hello!')

# 튜플 중첩
u = t, (1, 2, 3, 4, 5)
print(u)
# ((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))

# 튜플은 불변(immutable)입니다.
# t[0] = 88888
# TypeError: 'tuple' object does not support item assignment

# 하지만 가변(mutable) 객체를 포함할 수 있습니다.
v = ([1, 2, 3], [3, 2, 1])
print(v)
# ([1, 2, 3], [3, 2, 1])

v[0].append(4)
print(v)
# ([1, 2, 3, 4], [3, 2, 1])

# 하나의 항목으로 구성된 튜플은 값 뒤에 쉼표를 붙여서 만듭니다.
# 값 하나를 괄호로 둘러싸기만 하는 것으로는 충분하지 않습니다.
# 추합니다, 하지만 효과적입니다.
empty = ()
singleton = 'hello',
print(len(empty))
# 0

print(len(singleton))
# 1

print(singleton)
# ('hello',)

# 튜플 패킹
e = 12345, 54321, 'hello!'

# 튜플 시퀀스 언 패킹
# 다중 대입은 사실 튜플 패킹과 시퀀스 언 패킹의 조합일뿐이라는 것에 유의
x, y, z = e
print(x)
# 12345
