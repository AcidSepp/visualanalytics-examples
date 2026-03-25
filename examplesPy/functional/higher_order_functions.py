from typing import Callable

# snippet: main
def my_higher_order_function(my_function: Callable[[int], int]):
    my_function(1)


def my_other_higher_order_function() -> Callable[[int], int]:
    return lambda it: it + 1
# snippet: /main
