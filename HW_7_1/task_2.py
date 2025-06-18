
def type_check(func):

    def wrapper(*args, **kwargs):

        for arg in args:

            if not isinstance(arg, int):
                raise TypeError(f"Неверный тип аргумента {arg}. Ожидался <class 'int'>, получен {type(arg)}")

        for kwarg in kwargs:

            if not isinstance(kwarg, int):
                raise TypeError(f"Неверный тип аргумента {kwarg}. Ожидался <class 'int'>, получен {type(kwarg)}")

        return func(*args, **kwargs)

    return wrapper

@type_check
def add(a, b):
    return a + b

print(add(1,"3"))