#1
x1 = 5
y1 = 3
print("A1. %d" % x1**y1)

#2
print("A2. " + str(22 % 7))

#3
print("A3. " + str(3*1**3))

#4
print("A4. " + str(9//2))

#5
print("A5. " + str(6/2*(1+2)))

#6
x = True
y = False
z = False
if x or y and z:
    print("yes")
else:
    print("no")

#7
if not x or y:
    print(1)
elif not x or not y and z:
    print(2)
elif not x or y or not y and x:
    print(3)
else:
    print(4)

#8 雞兔同籠

n = 83
f = 240

r = (f - n * 2) // 2
c = n - r

print("A8. 雞有 %d 隻, 兔子有 %d 隻" % (c, r))
