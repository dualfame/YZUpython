h = 180
w = 80
try:
    bmi = w / (h/100)**2
    if bmi < 18 or bmi > 24:
        raise Exception("BMI超標" + str(bmi))
except Exception as e:
    print(e)
else:
    print(bmi)
