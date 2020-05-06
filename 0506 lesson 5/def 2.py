def getsum(*score):
    print(type(score), score)
    return sum(score)

print(getsum(10, 20, 30))
print(getsum())
