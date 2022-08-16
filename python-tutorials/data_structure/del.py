# del 문법: 리스트에서 값 대신에 인덱스를 사용해서 항목을 삭제하는 방법
a = [-1, 1, 66.25, 333, 333, 1234.5]

del a[0]
print(a)
# [1, 66.25, 333, 333, 1234.5]

del a[2:4]
print(a)
# [1, 66.25, 1234.5]

del a[:]
print(a)
# []

# 변수 자체를 삭제
del a

# print(a)
# NameError: name 'a' is not defined