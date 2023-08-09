def error_check(func):
    def inner(a, b):
        if b == 0:
            print("Cannot divide")
            return
        return func(a, b)
    return inner



@error_check
def divide(a, b):
    return a / b

print(divide(5, 1))