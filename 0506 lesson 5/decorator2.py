def login(password):
    def decorated(func):
        def check():
            if password == 123:
                print("Success")
                func()
            else:
                print("Wrong")
                return None
        return check
    return decorated

@login(password=12234)
def report():
    print("密件：今日頭條")

report()

# login(report, 123)()
# login(report, int(input('請輸入密碼:')))()
