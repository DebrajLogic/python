import time


def cache(fn):
    cache_value = {}

    def wrapper(*args, **kwargs):
        if args in cache_value:
            return cache_value[args]
        result = fn(*args, **kwargs)
        cache_value[args] = result
        return result
    return wrapper


@cache
def long_running_function(a, b):
    time.sleep(4)
    return a + b


print('fn output = ', long_running_function(3, 4))
print('fn output = ', long_running_function(3, 4))
print('fn output = ', long_running_function(2, 9))
print('fn output = ', long_running_function(2, 9))
