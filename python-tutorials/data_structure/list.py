# 리스트 메서드 사용 예제
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(fruits.count('apple'))
# 2
print(fruits.count('tangerine'))
# 0
print(fruits.index('banana'))
# 3
print(fruits.index('banana', 4))
# 6

fruits.reverse()

print(fruits)
# ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']

fruits.sort()

print(fruits)
# ['apple', 'apple', 'banana', 'banana', 'kiwi', 'orange', 'pear']

print(fruits.pop())
# pear

print(fruits)
# ['apple', 'apple', 'banana', 'banana', 'kiwi', 'orange']
