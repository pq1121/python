
def validate_range(min_value, max_value):

    def decorator(func):

        def wrapper(*args, **kwargs):

            for arg in args:
                if isinstance(arg, int or float):
                    if arg < min_value or arg > max_value:
                        raise ValueError(f"Аргумент value имеет значение {arg}, что выходит за пределы [{min_value}, {max_value}]")
                else:
                    raise TypeError("Неверный тип данных")

            for kwarg in kwargs:
                if isinstance(kwarg, int or float):
                    if kwarg < min_value or kwarg > max_value:
                        raise ValueError(f"Аргумент value имеет значение {kwarg}, что выходит за пределы [{min_value}, {max_value}]")
                else:
                    raise TypeError("Неверный тип данных")

            return func(*args, **kwargs)

        return wrapper

    return decorator

@validate_range(0,100)
def set_percentage(value):
    print(f"Установлено значение: {value}%")

set_percentage(50)
set_percentage(150)