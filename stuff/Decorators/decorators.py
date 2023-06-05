
def to_Uppercase(func):
    def wrapper(*args, **kwargs):
        value = func().upper()
        return value
    return wrapper

def to_List(func):
    def wrapper(*args, **kwargs):
        print("method called: "+str(func))
        value = []
        value[0:] = func(*args)
        return value
    return wrapper

def dec1(func):
    def wrapper():
        func()

def dec2(func):
    def wrapper():
        func()