import time
import logging


def measure_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"The execution time of {func.__name__} is {execution_time} seconds.")
        return result

    return wrapper


def convert_iterator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return tuple(result)

    return wrapper


def logged(exception, mode):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exception as e:
                if mode == "console":
                    logging.basicConfig(level=logging.INFO)
                elif mode == "file":
                    logging.basicConfig(filename='error.log', filemode='a', level=logging.INFO)
                logging.exception(e)

        return wrapper

    return decorator
