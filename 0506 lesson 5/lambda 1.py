def check_score(score):
    return "Pass" if score >= 60 else "Fail"

max = lambda x ,y : x if x > y else y
print('max=', max(80, 50))
print(check_score(max(80, 50)))

bmi = lambda w, h : w / (h/100)**2
print(bmi(85, 180))

name = lambda : print('d')
name()
