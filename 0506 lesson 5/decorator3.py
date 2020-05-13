def make_dress(func):
    def dress():
        print("穿衣服")
        func()
    return dress

def wear_shoe(func):
    def shoe():
        print("穿鞋")
        func()
    return shoe


@make_dress
@wear_shoe
def out():
    print("我出門了")


out()