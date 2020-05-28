x = 10
y = int(input("###"))
try:
    z = x / y
except ZeroDivisionError as e:
    print('分母不可為0', e)
else:
    print(z)
finally:
    print('MUST BE DONE')
