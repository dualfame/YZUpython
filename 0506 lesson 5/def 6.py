# 攝氏轉華氏
def ctof(n):
    cel_input = n
    f = cel_input * 9 / 5 + 32
    return f

print('華氏', ctof(100))

# 華氏轉攝氏
def ftoc(n):
    fent_input = n
    c = (fent_input - 32) * 5 / 9
    return c

print('攝氏', ftoc(100))

