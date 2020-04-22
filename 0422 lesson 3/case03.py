# 自訂函式
##有回傳值
def add(x, y):
    sum = x + y
    return sum
x=10
y=1

print(x+y)
print(add(x, y))

##無回傳值
def AddandPrint(x, y):
    sum = x + y
    print(sum)

AddandPrint(x, y)