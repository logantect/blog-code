# Dictionaries
# 파이썬에 내장된 또 하나의 쓸모있는 자료 형은 딕셔너리 입니다.
# 숫자들로 인덱싱되는 시퀀스와 달리, 딕셔너리는 키로 인덱싱되는데, 모든 불변형을 사용할 수 있다.
# 딕셔너리를(한 딕셔너리 안에서) 키가 중복되지 않는다는 제약 조건을 가진 키: 값 쌍의 집합으로 생각하는 것이 최선입니다.
import math

tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print(tel)
# {'jack': 4098, 'sape': 4139, 'guido': 4127}

print(tel['jack'])
# 4098

del tel['sape']
tel['irv'] = 4127
print(tel)
# {'jack': 4098, 'guido': 4127, 'irv': 4127}

# list(d)를 수행하면 딕셔너리에서 사용되고 있는 모든 키의 리스트를 삽입 순서대로 돌려준다.
print(list(tel))
# ['jack', 'guido', 'irv']

# 정렬을 원하면 list(d) 대신 sorted(d)
print(sorted(tel))
# ['guido', 'irv', 'jack']

# 하나의 키가 딕셔너리에 있는지 검사하려면, in 키워드들 사용하세요.
print('guido' in tel)
# True

print('jack' not in tel)
# False

# dict() 생성자는 키-값 쌍들의 시퀀스로 부터 직접 딕셔너리를 구성한다.
d = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print(d)
# {'sape': 4139, 'guido': 4127, 'jack': 4098}

# 딕셔너리 컴프리헨션은 임의의 키와 값 표현식들로 부터 딕셔너리를 만드는데 사용될 수 있다.
print({x: x ** 2 for x in (2, 4, 6)})
# {2: 4, 4: 16, 6: 36}

# items() 메서드를 사용하면 키와 거기에 대응하는 값을 동시에 얻을 수 있다.
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)
# gallahad the pure
# robin the brave

# 시퀀스를 루핑할 때, enumerate() 함수를 사용하면 위치 인덱스와 대응하는 값을 동시에 얻을 수 있다.
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)
# 0 tic
# 1 tac
# 2 toe

# 둘이나 그 이상의 시퀀스를 동시에 루핑하려면, zip() 함수로 엔트리들의 쌍을 만들 수 있다.
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}? It is {1}.'.format(q, a))
# What is your name? It is lancelot.
# What is your quest? It is the holy grail.
# What is your favorite color? It is blue.

# 시퀀스를 거꾸로 루핑하려면, 먼저 정방향으로 시퀀스를 지정한 다음에 reversed() 함수를 호출
for i in reversed(range(1, 10, 2)):
    print(i)
# 9
# 7
# 5
# 3
# 1

# 정렬된 순서로 시퀀스를 루핑하려면, sorted() 함수를 사용해서 소스를 변경하지 않고도 정렬된 새 리스트를 받을 수 있다.
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for i in sorted(basket):
    print(i)
# apple
# apple
# banana
# orange
# orange
# pear

# 시퀀스에 대해 set()과 sorted()를 함께 사용하는 것은 시퀀스의 고유 한 요소를 정렬된 순서로 루핑하는 관용적 방법이다.
for f in sorted(set(basket)):
    print(f)
# apple
# banana
# orange
# pear

# 루프를 돌고 있는 리스트를 변경하고픈 유혹을 느끼지만, 종종, 대신 새 리스트를 만드는 것이 더 간단하고 더 안전하다.
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)
print(filtered_data)
# [56.2, 51.7, 55.3, 52.5, 47.8]

# 비교의 결과나 다른 논리 표현식의 결과를 변수에 대입할 수 있다.
string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
non_null = string1 or string2 or string3
print(non_null)
# Trondheim