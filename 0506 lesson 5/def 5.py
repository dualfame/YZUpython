x = 0   #global var
y = 0   #global var
z = [0]
def changeX(n):
    x = n   # local var

def changeY(n):
    global y    #更改 global var
    y = n

def changeZ(m, n):
    m[0] = n

changeX(100)
print('x=', x)
changeY(100)
print('y=', y)
print('z=', z)
changeZ(z, 100)
print('z=', z)

