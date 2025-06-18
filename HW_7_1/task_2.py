
def type_check(type_num):

    def decorator(func):

        def wrapper(*args, **kwargs):

            for arg in args:

                if not isinstance(arg, type_num):
                    raise TypeError(f"Неверный тип аргумента {arg}. Ожидался <class 'int'>, получен {type(arg)}")

            for kwarg in kwargs:

                if not isinstance(kwarg, type_num):
                    raise TypeError(f"Неверный тип аргумента {kwarg}. Ожидался <class 'int'>, получен {type(kwarg)}")

            return func(*args, **kwargs)

        return wrapper

    return decorator

@type_check(int)
def add(a, b):
    return a + b

print(add(1,"3"))