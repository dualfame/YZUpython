def add(n):
    def calc(wt):
        return n * (1 + wt)
    return calc

x = add(150)

print("%.2f" % x(0.1))  # wt = 0.1
print("%.2f" % x(0.2))
print("%.2f" % x(0.3))
print("%.2f" % x(0.5))

# OR
print(add(150)(0.1))