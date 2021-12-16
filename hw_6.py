import sys
from datetime import datetime

original_write = sys.stdout.write


def my_write(string_text):
    now = [datetime.now().strftime('%Y-%m-%d %H:%M:%S')]
    if len(string_text.strip()) != 0:
        original_write(f'{now}: {string_text} \n')


def timed_output(function):
    def wrapper(*args, **kwargs):
        def my_write_2(string_text):
            now = [datetime.now().strftime('%Y-%m-%d %H:%M:%S')]
            if len(string_text.strip()) != 0:
                original_write(f'{now}: {string_text} \n')
        sys.stdout.write = my_write_2
        function(*args, **kwargs)
        sys.stdout.write = original_write
    return wrapper


@timed_output
def print_greeting(name):
    print(f'Hello, {name}!')


def redirect_output(filepath):
    def decorator(func):
        def wrapper(*args, **kwargs):
            original_out = sys.stdout
            sys.stdout = open(filepath, 'w')
            func(*args, **kwargs)
            sys.stdout.close()
            sys.stdout = original_out
        return wrapper
    return decorator


@redirect_output('./function_output.txt')
def calculate():
    for power in range(1, 5):
        for num in range(1, 20):
            print(num ** power, end=' ')
        print()


if __name__ == '__main__':
    sys.stdout.write = my_write
    print('1, 2, 3')
    sys.stdout.write = original_write
    print_greeting("Nikita")
    calculate()
