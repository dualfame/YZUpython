#循環控制
import random
while True:
    n = random.randint(1, 1000)
    if n == 500 :
        print(n)
        break
    if n % 7 != 0:
        continue

    print(n)


