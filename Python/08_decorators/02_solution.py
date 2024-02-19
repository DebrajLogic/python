
def debug(fn):
    def wrapper(*args, **kwargs):
        args_value = ', '.join(str(arg) for arg in args)
        kwargs_value = ', '.join(f'{k} : {v}' for k, v in kwargs.items())
        print(f'Calling: {fn.__name__} with args: {
              args_value or None} and kwargs: {kwargs_value or None}')
        return fn(*args, **kwargs)
    return wrapper


@debug
def hello():
    print('Hello!')


@debug
def greet(name, greeting='Hello'):
    return f'{greeting} {name}!'


hello()
print(greet('Debraj', greeting='Good Morning'))
