# 高階函數 advenced function
def add(x):
    return x + 1

def subs(x):
    return x - 1

def adv_func(func, x):
    return func(x)

x = 20
x = adv_func(add, x)
print(x)

z = [add, subs]
for z in func:
    print(adv_func(z, x))
