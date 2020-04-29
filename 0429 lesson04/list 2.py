'''
自動補牌機制
若不⾜ 6 (含)點需強迫補牌
若為 9 點（含）以上不需補牌
若為 7、8 點則策略補牌
若為 7 或 7.5 則看 A、2、3, J, Q, K 剩餘的牌 >= 12 (補)
若為 8 或 8.5 則看 A、2, J, Q, K 剩餘的牌 >= 10 (補)
'''
import random as r

poker = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'] * 4
r.shuffle(poker)
print(poker)
def getscore(points) :
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

#取牌
pc = []
pc.append(poker.pop(0))
#補牌
while True:
    score = getscore(pc)
    if score > 9: #不補牌
        break
    if score <= 6: #強制補牌
        pc.append(poker.pop(0))
        continue
    if 6 < score < 8:  # 6.5, 7, 7.5
        # A、2、3, J, Q, K 剩餘的牌 >= 12 (補)
        count = poker.count('A') + \
                poker.count(2) + \
                poker.count(3) + \
                poker.count('J') + \
                poker.count('Q') + \
                poker.count('K')
        if count >= 12:
            pc.append(poker.pop(0))
            continue
        else:
            break
    if 8 <= score < 9:  # 8, 8.5
        # A、2、J, Q, K 剩餘的牌 >= 10 (補)
        count = poker.count('A') + \
                poker.count(2) + \
                poker.count('J') + \
                poker.count('Q') + \
                poker.count('K')
        if count >= 10:
            pc.append(poker.pop(0))
            continue
        else:
            break


print(pc, getscore(pc))
