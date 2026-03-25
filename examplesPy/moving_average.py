# snippet: main
def moving_average(numbers: list[float], window_size: int) -> list[float]:
    samples = []
    result = []
    for value in numbers:
        while len(samples) >= window_size:
            samples.pop()
        samples.insert(0, value)
        result.append(sum(samples) / len(samples))
    return result


if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(moving_average(numbers, 3))
# snippet: /main
