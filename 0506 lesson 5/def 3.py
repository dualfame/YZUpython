def print_score(**exam):    #** 帶名字參數, dict
    print(type(exam), exam)
    print(exam.keys())
    print(exam.values())

print_score(國文=100, 數學=80, 英文=80)
