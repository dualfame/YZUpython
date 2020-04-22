import random as r #常用的inport指定代號

n = r.randint(1, 100)
if n % 2 == 0:
    print('%d 偶數' % n)
else:
    print('%d 竒數' % n)

#三元運算子
print('%d %s' % (n, "偶數" if n % 2 ==0 else "奇數"))
