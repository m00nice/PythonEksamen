
def to_Uppercase(func):
    def wrapper(*args, **kwargs):
        value = func().upper()
        return value
    return wrapper

def to_List(func):
    def wrapper(*args, **kwargs):
        value = []
        value[0:] = func(args[0])
        return value
    return wrapper
