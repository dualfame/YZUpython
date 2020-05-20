def print_func_name(func):
    def wrap():
        print("Now use function '{}'".format(func.__name__))
        func()
    return wrap


def dog_bark():
    print("Bark !!!")


def cat_miaow():
    print("Miaow ~~~")


if __name__ == "__main__":
    print_func_name(dog_bark)()
    # > Now use function 'dog_bark'
    # > Bark !!!

    print_func_name(cat_miaow)()
    # > Now use function 'cat_miaow'
    # > Miaow ~~~

## decorator @
def print_func_name(func):
    def warp():
        print("Now use function '{}'".format(func.__name__))
        func()

    return warp


@print_func_name
def dog_bark():
    print("Bark !!!")


@print_func_name
def cat_miaow():
    print("Miaow ~~~")


if __name__ == "__main__":
    dog_bark()
    # > Now use function 'dog_bark'
    # > Bark !!!

    cat_miaow()
    # > Now use function 'cat_miaow'
    # > Bark !!!