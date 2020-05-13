def message(text):
    text='YZU:' + text
    def print_text():
        print(text)
    return print_text

m = message("HELLO")
m()