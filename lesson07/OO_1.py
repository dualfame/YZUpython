#Class
# 1.存放資料
# 2.邏輯
# 3.封裝
# 4.繼承
# 5.多型

# data class

class Human:
    name = ''
    sex = ''
    age = 0

    def __str__(self):
        return self.name + "," + self.sex + "," + str(self.age)

class student(Human):
    number = 0
    grade = ''
    def __str__(self):
        return "," + str(self.number) + ", " + self.grade

print(__name__)
if __name__ == '__main__':
    h = Human()
    h.name = 'DW'
    h.sex = 'M'
    h.age = 18

    s = student()
    s.name = 'Ben'
    s.sex = 'M'
    s.age = 10
    s.number = 2
    s.grade = '4th'

print(h.name, h.sex, h.age)
print(h)
print(s)

