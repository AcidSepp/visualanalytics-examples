# snippet: main
import math

def window(numbers: list[int], window_size: int) -> list[list[int]]:
    result = []
    windows = math.ceil(len(numbers) / window_size)
    for index in range(windows):
        start_index = index * window_size
        stop_index = index * window_size + window_size
        result.append(numbers[start_index: stop_index])
    return result


if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    windows = window(numbers, 3)
    print(windows)
# snippet: /main
