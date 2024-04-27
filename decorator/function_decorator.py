import time
from typing import Any, Callable


def time_cost(func: Callable) -> Callable:
    def wrapper(*args, **kwargs) -> Any:
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'{func.__name__} took {int((end - start) * 1000)} ms')
        return result

    return wrapper


@time_cost
def some_op():
    print('Starting op')
    time.sleep(2)
    print('We are done')
    return 1


if __name__ == '__main__':
    some_op()
