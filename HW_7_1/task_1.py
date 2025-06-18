def count_calls(func):
    count = 0
    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        print(f"Функция {func.__name__} вызвана {count} раз(а)")
        func(*args, **kwargs)
        pass

    return wrapper

@count_calls
def greet(name):
    print(f"Привет, {name}!")

greet("Первый")
greet("Второй")