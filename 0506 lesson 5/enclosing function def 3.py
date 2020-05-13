def message(text):
    text='YZU:' + text
    def print_text():
        print(text)
    return print_text() # 有()，直接執行

m = message("HELLO")
#m()