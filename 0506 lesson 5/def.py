def add(x=1, y=2, z=None):  #可以設初始值
    if z == None:
        return x + y
    return (x + y) * z

print(add())
print(add(5))   # 改x=5
print(add(y=10))    # 改y=10
print(10*add())
print(add(z=10))
print(add(2, 3, 5))
print(add(2, 3))

