from functools import wraps

def basic_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Before {func.__name__}")
        func(*args, **kwargs)
        print(f"After {func.__name__}")
    return wrapper

@basic_decorator
def greet_user(name):
    print(f"Hello {name}, welcome to python!")

if __name__ == "__main__":
    user_name = input("Enter your name:\t")
    greet_user(user_name)