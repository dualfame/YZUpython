def keynum():
    x = 10
    try:
        y = int(input('Key a #'))
        z = x / y
    except ZeroDivisionError as e:
        print('分母不可為0, 請重新輸入', e)
        keynum()
    except ValueError as e:
        print('請輸入數字', e)
        keynum()
    except Exception as e:
        print('Undefine Error', e)
    except (ZeroDivisionError, )
    else:
        print(z)
if __name__ == '__main__':
    keynum()
