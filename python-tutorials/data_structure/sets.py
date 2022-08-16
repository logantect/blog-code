# Set - 중복되는 요소가 없는 순서 없는 컬렉션
# 기본적인 용도는 멤버십 검사와 중복 엔트리 제거입니다.
# 집합 객체는 합집합, 교집합, 차집합, 대칭 차집합과 같은 수학적인 연산들도 지원합니다.
# 집합을 만들려면 set() 을 사용해야 합니다. {} 가 아닙니다.
# {} 는 빈 딕셔너리를 만듭니다.
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)
# {'orange', 'pear', 'banana', 'apple'}

print('orange' in basket)
# True

print('crabgrass' in basket)
# False

# 두 단어의 고유한 문자에 대한 집합 연산
# 출력 순서는 순서가 없기 때문에 실행할 때마다 변경될 수 있다.
a = set('abracadabra')
b = set('alacazam')
print(a)
# {'b', 'c', 'a', 'r', 'd'}

print(b)
# {'l', 'z', 'c', 'm', 'a'}

print(a - b)  # 차집합: a 에는 있지만 b에는 없는 문자
# {'b', 'r', 'd'}

print(a | b)  # 합집합: a 또는 b의 문자
# {'b', 'r', 'l', 'z', 'c', 'd', 'm', 'a'}

print(a & b)  # 교집합: a와 b에 모두 있는 문자
# {'c', 'a'}

print(a ^ b)  # 대칭 차집합: a또는 b에 있는 문자 인데 둘다에는 없는 문자
# {'b', 'r', 'z', 'd', 'm', 'l'}

# 리스트 컴프리헨션과 유사하게, 집합 컴프리헨션도 지원된다.
print({x for x in 'abracadabra' if x not in 'abc'})
# {'r', 'd'}
