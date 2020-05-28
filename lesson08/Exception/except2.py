x = 10
y = int(input("###"))
try:
    z = x / y
except ZeroDivisionError as e:
    print('分母不可為0', e)
except ValueError as v:
    print('請輸入數字', v)
else:
    print(z)