#set 不重複數組
import random as r

lotto = set()
lotto.add(1)
lotto.add(1)
lotto.add(1)
lotto.add(2)
lotto.add(3)
print(lotto)

lotto539 = set()
while len(lotto539) < 5:
    lotto539.add(r.randint(1,39))
print(sorted(lotto539))
