# y=a*x+b

# a = float(input("a=?"))
# b = float(input("b=?"))
# for x in range (0, 12, 3):
#     y = a*x + b
#     print("x = %d, y = %d" %(x, y))


import numpy as np
for Xi in range(1, 10, 1):
    for Yi in range(1, 10, 1):
        tt = Xi*Yi
        print(tt)

a1 = np.arange(tt)
a2 = np.arange(tt).reshape(9, 9, 1)
a3 = np.arange(tt).reshape(9, 1, 9)
a4 = np.arange(tt).reshape(1, 9, 9)
print(a1, a2, a3, a4, sep='\n')
