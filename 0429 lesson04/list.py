import operator
import random
poker1 = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
poker2 = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']

#串列比較 operator.eq(Python 3.x版), cmp(Python 2.x版)
print(operator.eq(poker1, poker2))

poker = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'] * 4
print(poker)
print(len(poker))
print(poker.count('K'))

#洗牌
random.shuffle(poker)
print(poker)
print(len(poker))

#抽第一張牌
card = poker.pop(0)
print('抽第一張牌', card)
print(poker)
print(len(poker))

#計算前三張的點數; A=1, J,Q,K =0.5
print(poker[:3])
def score(points) :
    sum = 0
    for p in points:
        if p == 'A':
            sum = sum + 1
            continue

        if p == 'J' or p =='Q' or p == 'K':
            sum = sum + 0.5
            continue

        sum = sum + p
    return sum
print(score(poker[:3]))
print('K' in poker)