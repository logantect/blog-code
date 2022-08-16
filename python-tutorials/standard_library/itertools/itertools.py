from itertools import permutations, product, combinations, combinations_with_replacement

data = ['A', 'B', 'C']  # 데이터 준비

# permutations는 리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아 일렬로 나열하는 모든 경우(순열)를 계산해준다.
# 모든 순열 구하기
print(list(permutations(data, 3)))
# [('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')]

# combinations는 리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아 순서를 고려하지 않고 나열하는 모든 경우(조합)를 계산한다.
# 2개를 뽑는 모든 조합 구하기
print(list(combinations(data, 2)))
# [('A', 'B'), ('A', 'C'), ('B', 'C')]

# product는 permutations와 같이 리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아 일렬로 나열하는 모든 경우(순열)를 계산한다.
# 다만, 원소를 중복하여 뽑는다.
# 2개를 뽑는 모든 순열 구하기(중복 허용)
print(list(product(data, repeat=2)))
# [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'), ('B', 'C'), ('C', 'A'), ('C', 'B'), ('C', 'C')]

# combinations_with_replacement는 combinations와 같이 리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아 순서를 고려하지 않고 나열하는 모든 경우(조합)를 계산한다.
# 다만, 원소를 중복해서 뽑는다.
# 2개를 뽑는 모든 조합 구하기(중복 허용)
print(list(combinations_with_replacement(data, 2)))
