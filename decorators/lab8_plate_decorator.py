import time


def measure_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"The execution time of {func.__name__} is {execution_time} seconds.")
        return result

    return wrapper


def print_iterable_length(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if hasattr(result, "__iter__"):
            length = sum(1 for _ in result)
        else:
            length = 1
        print(f"The length of the iterable object is: {length}")
        return result

    return wrapper
