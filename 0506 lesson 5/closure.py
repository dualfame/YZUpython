def make(n):
    def multi(x):
        return n * x
    return multi

m3 = make(3)
m5 = make(5)

print(m3(6))    # 3*6
print(m3(m5(6)))    #3*5*6
