# class Book:
#     pass
#
# b = Book()
# b.name = 'python'
# b.price = 500
# print(b.name, b.price)

class Book:
    def __getattr__(self, name):
        try:
            return object.__getattribute__(name)
        except:
            return name + ' is not found!'

b = Book()
print(b.booktitle)
b.booktitle = 'Python'
print(b.booktitle)
