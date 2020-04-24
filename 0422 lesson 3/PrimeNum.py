# n 是質數?

n = int(input(" 輸入數字"))
check = "質數"
for i in range(2, n//2+1):
    print("%d / %d 餘數 %d" % (n, i, n % i))
    if n % i == 0:
        check = "非質數"
        break;

print(n, "是", check)

# 2~50 誰是質數
def isprime(n):
    check = True
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            check = False
            break;
        return check

for i in range(2, 51):
    print(i, "質數" if isprime(i) else "非質數")
